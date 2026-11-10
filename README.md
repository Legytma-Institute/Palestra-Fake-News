# Palestra: Fake News e Golpes Virtuais

Material da palestra **"Pare antes de compartilhar"**, para alunos do ensino médio da Escola Estadual Marieta Telles Machado (10/11/2026), por Alex Manoel Ferreira Silva.

## Conteúdo

### Apresentações
| Pasta | O que é |
|---|---|
| [`apresentacoes/pare-antes-de-compartilhar/`](apresentacoes/pare-antes-de-compartilhar/) | Apresentação principal: 43 slides em 9 blocos (abertura, desinformação, por que acreditamos, P.I.R.A. e leitura lateral, quiz, IA e deepfakes, golpes, se você cair, fechamento), com notas do apresentador. Usa o design system Verifica. |
| [`apresentacoes/riscos-online-para-adolescentes/`](apresentacoes/riscos-online-para-adolescentes/) | Apresentação anterior (03/11/2026): 10 slides sobre sete riscos online para adolescentes. |

Cada pasta tem `deck.json` (título, ordem, seções, fontes), `slides/<id>.html` (um slide por arquivo, 1920×1080, com notas em `<aside>`) e `apresentacao.html`, uma versão navegável offline: abra no navegador e use ←/→, **N** para notas e **F** para tela cheia.

### Documentos de apoio (`docs/`)
| Arquivo | O que é |
|---|---|
| [`material-de-apoio.md`](docs/material-de-apoio.md) | Material de apoio com base científica: roteiro, dados, checklist P.I.R.A., golpes, prompt de IA, dinâmicas e referências comentadas. |
| [`real-ou-ia-par-de-imagens.md`](docs/real-ou-ia-par-de-imagens.md) | Pesquisa do par de imagens checadas para o "Real ou IA?" da abertura. |
| [`leitura-lateral-ilsi-brasil.md`](docs/leitura-lateral-ilsi-brasil.md) | Caso do ILSI Brasil para a dinâmica de leitura lateral, com alternativas e roteiro. |
| [`pesquisa-adolescentes-seguros-no-online.md`](docs/pesquisa-adolescentes-seguros-no-online.md) | Pesquisa "Adolescentes seguros no online" (03/11/2026): riscos, estudos, proteção, leis e canais de ajuda. |
| [`prompt-checagem-completo.md`](docs/prompt-checagem-completo.md) | Prompt para checar notícias com IA, versão completa (computador). |
| [`prompt-checagem-curto.md`](docs/prompt-checagem-curto.md) | Prompt para checar notícias com IA, versão curta (celular, Meta AI no WhatsApp). |
| [`prompt-checagem-completo.txt`](docs/prompt-checagem-completo.txt) e [`prompt-checagem-curto.txt`](docs/prompt-checagem-curto.txt) | Os mesmos prompts só em texto puro, para os QR Codes. |

#### Links para os QR Codes
Estes endereços abrem só o texto do prompt, sem a página do GitHub:
- Completo: https://raw.githubusercontent.com/Legytma-Institute/Palestra-Fake-News/main/docs/prompt-checagem-completo.txt
- Curto: https://raw.githubusercontent.com/Legytma-Institute/Palestra-Fake-News/main/docs/prompt-checagem-curto.txt

Se editar um prompt, altere o `.md` e o `.txt` juntos.

### Guia do aluno (`guia-do-aluno/`)
Guia de bolso impresso, 4 páginas A4: [`guia-pare-antes-de-compartilhar.pdf`](guia-do-aluno/guia-pare-antes-de-compartilhar.pdf), com a fonte editável em HTML. Detalhes em [`guia-do-aluno/README.md`](guia-do-aluno/README.md).

### Design system (`design-system/verifica/`)
Tokens (`tokens.json`), guia (`README.md`), capa (`components/Cover/preview.html`) e índice (`design-system.json`) do sistema visual "Verifica": um jornal de papel sendo checado.

## Regerar o HTML das apresentações

```bash
python3 tools/build_deck.py apresentacoes/pare-antes-de-compartilhar
python3 tools/build_deck.py apresentacoes/riscos-online-para-adolescentes
```

O script também baixa imagens que faltem, se `assets/assets.json` indicar uma `url`. Créditos e uso das imagens: [`apresentacoes/pare-antes-de-compartilhar/assets/README.md`](apresentacoes/pare-antes-de-compartilhar/assets/README.md).

## Antes da palestra
Dados, leis (MED 2.0, ECA Digital, Lei 15.123/2025) e links das checagens mudam: confira na véspera, como indicam os próprios documentos.
