#!/usr/bin/env python3
"""Validação do site netstart.github.io antes do commit (só stdlib).

Confere o que está indexado (git diff --cached) e o conteúdo dos arquivos no disco:
política de privacidade estável na raiz, datas PT/EN/Markdown iguais, app-ads.txt,
redirects das URLs antigas, .nojekyll e, se possível, a checagem cruzada com o hyakki.
Sai com código 1 em qualquer erro.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POLICY = "privacy-policy.html"
POLICY_MD = os.path.join("hyakki", "privacy-policy.md")
REDIRECTS = [os.path.join("games", "hyakki", "privacy-policy.html"),
             os.path.join("hyakki", "privacy-policy.html")]
PACKAGE = "io.github.netstart.hyakki"
MESES = {"janeiro": 1, "fevereiro": 2, "março": 3, "marco": 3, "abril": 4, "maio": 5, "junho": 6,
         "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}

erros = []
avisos = []


def erro(msg):
    erros.append(msg)


def aviso(msg):
    avisos.append(msg)


def ler(rel):
    caminho = os.path.join(ROOT, rel)
    if not os.path.isfile(caminho):
        return None
    with open(caminho, encoding="utf-8-sig") as f:
        return f.read()


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def mudancas_indexadas():
    """Devolve lista de (status, caminho_antigo, caminho_novo) do índice."""
    r = git("diff", "--cached", "--name-status", "-M")
    if r.returncode != 0:
        aviso("não consegui ler o índice do git: " + r.stderr.strip())
        return []
    linhas = []
    for linha in r.stdout.splitlines():
        partes = linha.split("\t")
        if not partes or not partes[0]:
            continue
        status = partes[0][0]
        if status in ("R", "C") and len(partes) >= 3:
            linhas.append((status, partes[1].replace("/", os.sep), partes[2].replace("/", os.sep)))
        elif len(partes) >= 2:
            linhas.append((status, partes[1].replace("/", os.sep), partes[1].replace("/", os.sep)))
    return linhas


def checar_politica():
    for status, antigo, novo in mudancas_indexadas():
        if antigo == POLICY and status == "D":
            erro(f"{POLICY} está sendo apagado no commit; a Play Console exige a URL estável.")
        if antigo == POLICY and status == "R":
            erro(f"{POLICY} está sendo renomeado para {novo}; a Play Console exige a URL estável.")
    html = ler(POLICY)
    if html is None:
        erro(f"{POLICY} não existe na raiz do site.")
        return None
    for trecho, descricao in [('id="pt"', 'a seção id="pt"'), ('id="en"', 'a seção id="en"'),
                              (PACKAGE, f"o pacote {PACKAGE}"),
                              ("mailto:netstart@gmail.com", "o link mailto:netstart@gmail.com")]:
        if trecho not in html:
            erro(f"{POLICY} não contém {descricao}.")
    datas = re.findall(r'<time\s+datetime="(\d{4}-\d{2}-\d{2})"', html)
    if len(datas) < 2:
        erro(f'{POLICY} deveria ter duas datas <time datetime="AAAA-MM-DD"> (PT e EN); achei {len(datas)}.')
        return datas[0] if datas else None
    if len(set(datas)) != 1:
        erro(f"as datas das seções PT e EN de {POLICY} divergem: {', '.join(datas)}.")
        return None
    return datas[0]


def checar_markdown(data_html):
    md = ler(POLICY_MD)
    if md is None:
        return
    m = re.search(r"^Última atualização:\s*(\d{1,2}) de (\S+) de (\d{4})\s*$", md, re.M)
    if not m:
        erro(f"{POLICY_MD} não tem a linha 'Última atualização: D de mês de AAAA'.")
        return
    dia, mes_nome, ano = int(m.group(1)), m.group(2).lower(), int(m.group(3))
    mes = MESES.get(mes_nome)
    if mes is None:
        erro(f"{POLICY_MD}: mês '{mes_nome}' não reconhecido na linha 'Última atualização'.")
        return
    data_md = f"{ano:04d}-{mes:02d}-{dia:02d}"
    if data_html and data_md != data_html:
        erro(f"data de {POLICY_MD} ({data_md}) difere da data de {POLICY} ({data_html}).")


def checar_app_ads():
    txt = ler("app-ads.txt")
    if txt is None:
        erro("app-ads.txt não existe na raiz do site.")
        return
    if not re.search(r"^google\.com,\s*pub-\d+,\s*DIRECT,\s*f08c47fec0942fa0\s*$", txt, re.M):
        erro("app-ads.txt não tem a linha 'google.com, pub-<dígitos>, DIRECT, f08c47fec0942fa0'.")


def checar_redirects():
    for rel in REDIRECTS:
        html = ler(rel)
        if html is None:
            erro(f"{rel} não existe (deveria ser um redirect para /privacy-policy.html).")
        elif "url=/privacy-policy.html" not in html:
            erro(f"{rel} não redireciona para /privacy-policy.html (falta 'url=/privacy-policy.html').")


def checar_nojekyll():
    if not os.path.isfile(os.path.join(ROOT, ".nojekyll")):
        erro(".nojekyll não existe na raiz do site.")


def checar_hyakki():
    hyakki = os.environ.get("HYAKKI_DIR") or os.path.join(os.path.dirname(ROOT), "hyakki")
    hyakki = os.path.abspath(hyakki)
    script = os.path.join(hyakki, "tools", "sync_site.py")
    if not os.path.isdir(hyakki):
        aviso(f"repositório do hyakki não encontrado em {hyakki}; checagem cruzada pulada.")
        return
    if not os.path.isfile(script):
        aviso(f"{script} não existe; checagem cruzada com o hyakki pulada.")
        return
    env = dict(os.environ, NETSTART_SITE_DIR=ROOT)
    r = subprocess.run([sys.executable, "-I", os.path.join("tools", "sync_site.py"), "--check"],
                       cwd=hyakki, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    saida = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        erro("tools/sync_site.py --check do hyakki falhou:\n" + saida)
    elif saida:
        print(saida)


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    data_html = checar_politica()
    checar_markdown(data_html)
    checar_app_ads()
    checar_redirects()
    checar_nojekyll()
    checar_hyakki()
    for a in avisos:
        print("AVISO: " + a)
    if erros:
        for e in erros:
            print("ERRO: " + e, file=sys.stderr)
        print(f"check_site: {len(erros)} erro(s); commit reprovado.", file=sys.stderr)
        return 1
    print("check_site: tudo certo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
