# Imagens da apresentação

| Arquivo | Slide | No repositório? |
|---|---|---|
| `ilsi-brasil-print.png` | Dinâmica de leitura lateral | Sim — print do site do ILSI Brasil (10/11/2026), usado para crítica e estudo |
| `qr-prompt-checagem-completo.png` | "Leve um checador no bolso" | Sim — QR Code que abre `docs/prompt-checagem-completo.txt` em texto puro |
| `real-ou-ia-a-gize.jpg` | "Real ou IA?" — imagem A (falsa) | **Não** |
| `real-ou-ia-b-etna.jpg` | "Real ou IA?" — imagem B (foto real de Davide Basile) | **Não** |

As duas imagens do "Real ou IA?" ficam fora do repositório de propósito: a foto do Etna é obra protegida do fotógrafo Davide Basile, e a pesquisa da palestra recomenda não distribuir o arquivo fora do slide (Lei 9.610/98, art. 46, III — citação para estudo e crítica, com crédito). A imagem de Gizé tem autoria desconhecida.

Elas continuam na apresentação publicada no Claude. Para gerar o `apresentacao.html` local com elas, salve os dois arquivos aqui com os nomes acima (estão no `.gitignore`) e rode `python3 tools/build_deck.py apresentacoes/pare-antes-de-compartilhar`. Sem eles, o slide mostra só o texto alternativo.
