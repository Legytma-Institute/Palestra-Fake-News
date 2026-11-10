# Guia de bolso do aluno

Guia impresso para os alunos levarem para casa: 4 páginas A4, fundo branco, para imprimir frente e verso (2 folhas por aluno).

| Arquivo | O que é |
|---|---|
| `guia-pare-antes-de-compartilhar.pdf` | O guia pronto para imprimir |
| `guia-do-aluno.html` | Fonte editável do guia |
| `qr-prompt-completo-txt.png` | QR Code usado na página 3; abre `docs/prompt-checagem-completo.txt` em texto puro |

**Páginas**
1. Como identificar: checklist P.I.R.A., leitura lateral, sinais de alerta, armadilhas do cérebro, ferramentas grátis e a regra de ouro.
2. Golpes mais comuns entre jovens, kit básico de proteção, "desconfiar de tudo também atrapalha" e o sanduíche da verdade.
3. Se cair num golpe: passos, ameaça com foto íntima, deepfake e IA, onde pedir ajuda e o prompt curto com o QR Code.
4. Prompt completo impresso e as referências das dicas.

Para imprimir só uma folha frente e verso, imprima as páginas 1 a 2 ou 1 a 3 conforme a necessidade (a página 4 é opcional).

## Regerar o PDF depois de editar o HTML

```bash
cd guia-do-aluno
python3 - <<'PY'
import asyncio, os
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.emulate_media(media="print")
        await pg.goto("file://" + os.path.abspath("guia-do-aluno.html"), wait_until="networkidle")
        await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(800)
        await pg.pdf(path="guia-pare-antes-de-compartilhar.pdf", format="A4", print_background=True, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
PY
```

Antes de rodar as cópias, escaneie o QR Code impresso com um celular.
