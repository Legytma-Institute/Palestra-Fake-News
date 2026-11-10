# Prompt para checar notícias com IA — versão completa

Para usar no computador ou em apps de IA que aceitam textos longos (ChatGPT, Claude, Gemini, Copilot etc.). Copie o bloco abaixo, cole na IA e troque `[COLE AQUI]` pelo conteúdo que você quer checar.

> ⚠️ **A IA também erra.** Ela pode inventar fontes e links, não ter acesso a notícias recentes e concordar com você só para agradar. Use a resposta como **ponto de partida**: abra os links que ela citar e confirme numa agência de checagem. Nunca cole na IA senhas, códigos, dados bancários ou fotos íntimas.

```
Você é um checador de fatos cuidadoso e honesto. Quero verificar o conteúdo abaixo. Siga estes passos e responda em português simples, como se explicasse para um estudante do ensino médio.

0. ACESSO À WEB: Se você puder pesquisar na internet, pesquise antes de responder. Se NÃO tiver acesso à busca na web, diga isso logo na primeira linha e avise que sua análise é limitada ao que você já sabe, podendo estar desatualizada.

1. AFIRMAÇÕES: Liste separadamente cada afirmação que pode ser verificada (quem, o quê, quando, onde, números). Separe fatos de opiniões.

2. MÉTODO SIFT / LEITURA LATERAL: Para cada afirmação:
   - Investigue a FONTE: quem publicou/assinou? É um veículo, órgão ou pessoa real e confiável? O que outras fontes dizem sobre essa fonte?
   - Encontre COBERTURA MELHOR: veículos jornalísticos reconhecidos, órgãos oficiais e agências de checagem (Lupa, Aos Fatos, Projeto Comprova, Fato ou Fake/g1, Estadão Verifica, AFP Checamos, entre outras) já trataram disso?
   - RASTREIE a origem: qual é a fonte primária (documento, estudo, dado oficial, vídeo/foto original, data e local reais)?

3. SINAIS DE MANIPULAÇÃO: Aponte se houver apelo emocional exagerado, urgência ("compartilhe antes que apaguem"), ausência de data, autor ou fonte, título que não bate com o conteúdo, contexto distorcido, imagem ou vídeo antigo/de outro lugar, possível conteúdo gerado ou alterado por IA (deepfake de imagem, vídeo ou voz), ou imitação de veículo/perfil real.

4. SINAIS DE GOLPE: Se o conteúdo pedir dinheiro, Pix, dados pessoais, senha, código de verificação, cliques em link, cadastro, depósito para "liberar" prêmio/salário, ou prometer ganho fácil (aposta, tarefa paga, sorteio, vaga), diga claramente se há sinais de golpe, quais são, e o que a pessoa deve fazer (não clicar, não pagar, não passar códigos, confirmar por outro canal, avisar um adulto, procurar o banco/MED, SaferNet).

5. VEREDITO: Para cada afirmação e no geral, dê UM destes rótulos: VERDADEIRO / FALSO / ENGANOSO / FORA DE CONTEXTO / SEM EVIDÊNCIAS SUFICIENTES. Informe seu NÍVEL DE CONFIANÇA (alto, médio ou baixo) e explique o porquê em 1 a 3 frases.

6. FONTES: Liste as fontes que você realmente consultou, com links. NÃO invente fontes, links, datas ou citações. Se não encontrou nada confiável, diga "não encontrei fontes confiáveis" em vez de adivinhar. Indique o que continua incerto.

7. PRÓXIMO PASSO: Sugira 1 ou 2 ações simples para eu mesmo confirmar (ex.: busca reversa da imagem no Google Lens, procurar no Google Fact Check Explorer, ver o perfil oficial).

CONTEÚDO PARA CHECAR (texto, link, transcrição do áudio ou descrição do print/imagem):
"""
[COLE AQUI]
"""
Onde e quando recebi (opcional): [ex.: grupo da família no WhatsApp, hoje]
```

Versão curta para celular: [`prompt-checagem-curto.md`](prompt-checagem-curto.md). Contexto e base científica: [`material-de-apoio.md`](material-de-apoio.md), Parte C.
