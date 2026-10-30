# netstart.github.io

- Regra de ouro: a fonte da política de privacidade é `hyakki/privacy-policy.md` e a página publicada é `privacy-policy.html` na raiz. Toda mudança atualiza as duas, com o mesmo conteúdo e a mesma data (`Última atualização` no .md e os dois `<time datetime>` do .html).
- Nunca apagar nem renomear `privacy-policy.html` nem `app-ads.txt`: a Play Console e o AdMob dependem dessas URLs.
- `app-ads.txt` é gerado pelo repositório do jogo (hyakki, `tools/sync_site.py`); não editar à mão.
- `hyakki/privacy-policy.html` e `games/hyakki/privacy-policy.html` são só redirects para `/privacy-policy.html`.
- O hook `.githooks/pre-commit` (instalado com `.githooks/install.ps1` ou `.sh`) valida tudo isso; não o contorne.
- Textos em português. Commit aqui e `git push` para publicar no GitHub Pages.
