# netstart.github.io

Site estático publicado pelo GitHub Pages a partir da raiz da branch `main`:
<https://netstart.github.io>. Hospeda o catálogo de jogos, a landing do Hyakki, a política de
privacidade e o `app-ads.txt`.

## Mapa dos arquivos

| Caminho | Função |
| --- | --- |
| `index.html` | Catálogo dos jogos. |
| `privacy-policy.html` | Política de privacidade do Hyakki (PT/EN). URL oficial na Play Console e no jogo: `https://netstart.github.io/privacy-policy.html`. Nunca apagar nem renomear. |
| `hyakki/privacy-policy.md` | Fonte em Markdown da política. Mantenha `.md` e `.html` com o mesmo conteúdo e a mesma data. |
| `hyakki/index.html` | Landing do jogo Hyakki. |
| `hyakki/privacy-policy.html`, `games/hyakki/privacy-policy.html` | URLs antigas: só redirecionam para `/privacy-policy.html`. |
| `app-ads.txt` | Autorização do AdMob. Gerado pelo repositório do jogo (`tools/sync_site.py` do hyakki); não editar à mão. |
| `.nojekyll` | Desliga o Jekyll do Pages (o site é estático e tem `.md` que não deve ser processado). |
| `.githooks/` | Hook de pre-commit (`check_site.py`) e instaladores. |

## Regra

Tudo o que é publicado em netstart.github.io é editado e commitado **aqui**. O repositório do jogo
(hyakki) não guarda cópias das páginas: ele só gera o `app-ads.txt` via `tools/sync_site.py` e aponta
para este repositório.

## Hook de pre-commit

Uma vez por clone, instale o hook versionado:

```powershell
.\.githooks\install.ps1
```

ou

```sh
sh .githooks/install.sh
```

Isso roda `git config core.hooksPath .githooks`. A cada commit, `check_site.py` confere a política
(existência, seções PT/EN, pacote, e-mail, datas iguais no HTML e no Markdown), o `app-ads.txt`, os
redirects, o `.nojekyll` e, se o hyakki estiver na pasta irmã `../hyakki` (ou em `$HYAKKI_DIR`), roda
`tools/sync_site.py --check` dele.

## Publicar

Depois de commitar, é preciso `git push` para o GitHub Pages publicar a nova versão.
