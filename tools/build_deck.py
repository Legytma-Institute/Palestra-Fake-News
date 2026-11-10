#!/usr/bin/env python3
"""Gera um HTML único e navegável (offline) a partir de uma pasta de apresentação.

Uso: python3 tools/build_deck.py apresentacoes/<deck>
Saída: apresentacoes/<deck>/apresentacao.html

Lê deck.json (ordem, título, fontes), junta os slides de slides/<id>.html,
troca referências /_blob/<id> pelos arquivos locais listados em assets/assets.json
e mostra as notas do apresentador (<aside>) com a tecla N.

Cada entrada de assets.json pode ser só o caminho local
    "/_blob/<id>": "assets/foto.png"
ou um objeto com o endereço de onde baixar a imagem quando ela não está no repositório
    "/_blob/<id>": {"arquivo": "assets/foto.jpg", "url": "https://..."}
Imagens que faltam e têm "url" são baixadas antes de gerar o HTML.
"""
import html, json, re, sys, urllib.request
from pathlib import Path

deck_dir = Path(sys.argv[1])
deck = json.loads((deck_dir / "deck.json").read_text(encoding="utf-8"))
assets_map = {}
amap = deck_dir / "assets" / "assets.json"
if amap.exists():
    for blob, entry in json.loads(amap.read_text(encoding="utf-8")).items():
        if isinstance(entry, str):
            entry = {"arquivo": entry}
        local = deck_dir / entry["arquivo"]
        url = entry.get("url")
        if not local.exists() and url:
            print(f"baixando {entry['arquivo']} de {url}")
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "build_deck/1.0"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    local.write_bytes(r.read())
            except Exception as e:
                print(f"  falhou: {e}")
        if not local.exists():
            print(f"aviso: {entry['arquivo']} não encontrado; o slide mostrará só o texto alternativo")
        assets_map[blob] = entry["arquivo"]

fonts = "\n".join(
    f'<link rel="stylesheet" href="{html.escape(f["href"])}">'
    for f in deck.get("faces", {}).values() if f.get("href")
)

slides = []
for sid in deck["order"]:
    src = (deck_dir / "slides" / f"{sid}.html").read_text(encoding="utf-8")
    for blob, local in assets_map.items():
        src = src.replace(blob, local)
    notes = ""
    m = re.search(r"<aside>(.*?)</aside>", src, re.S)
    if m:
        notes = m.group(1).strip()
        src = src[: m.start()] + src[m.end():]
    slides.append(
        f'<div class="frame"><div class="stage">{src}</div>'
        f'<div class="notes">{html.escape(notes).replace(chr(10), "<br>")}</div></div>'
    )

page = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(deck["title"])}</title>
{fonts}
<style>
html,body{{margin:0;height:100%;background:#111;overflow:hidden}}
*{{box-sizing:border-box}} h1,h2,h3,p,ul,ol,table{{margin:0}}
.frame{{display:none;position:absolute;inset:0}}
.frame.on{{display:block}}
.stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:center}}
.stage>section{{position:relative;width:1920px;height:1080px;overflow:hidden}}
.notes{{display:none;position:absolute;left:0;right:0;bottom:0;max-height:35%;overflow:auto;
  background:rgba(0,0,0,.85);color:#eee;font:16px/1.5 system-ui,sans-serif;padding:16px 24px}}
body.show-notes .frame.on .notes{{display:block}}
.hud{{position:fixed;right:12px;bottom:8px;color:#888;font:12px system-ui,sans-serif}}
/* Revelação por clique (data-build-in="efeito passo"), como na apresentação publicada */
[data-build-in]{{transition:opacity .35s ease,scale .35s cubic-bezier(.3,1.6,.5,1),translate .35s ease}}
[data-build-in].oculto{{opacity:0;pointer-events:none}}
[data-build-in^="pop"].oculto{{scale:.5}}
[data-build-in^="rise"].oculto{{translate:0 40px}}
</style></head><body>
{"".join(slides)}
<div class="hud" id="hud"></div>
<script>
const frames=[...document.querySelectorAll('.frame')];let i=0,passo=0;
// Passos de cada slide: elementos com o mesmo número aparecem juntos, em ordem crescente.
const passos=frames.map(f=>{{const g={{}};
  f.querySelectorAll('[data-build-in]').forEach(el=>{{const n=parseInt(el.dataset.buildIn.split(/\\s+/)[1])||1;(g[n]=g[n]||[]).push(el);}});
  return Object.keys(g).map(Number).sort((a,b)=>a-b).map(n=>g[n]);}});
function revelar(k,ate){{passos[k].forEach((grupo,j)=>grupo.forEach(el=>el.classList.toggle('oculto',j>=ate)));}}
function fit(){{const s=Math.min(innerWidth/1920,innerHeight/1080);
  document.querySelectorAll('.stage').forEach(e=>e.style.transform=`translate(-50%,-50%) scale(${{s}})`);}}
function show(n,completo){{i=Math.max(0,Math.min(frames.length-1,n));passo=completo?passos[i].length:0;revelar(i,passo);
  frames.forEach((f,k)=>f.classList.toggle('on',k===i));
  document.getElementById('hud').textContent=`${{i+1}} / ${{frames.length}} · ←/→ navegar · N notas · F tela cheia`;
  history.replaceState(null,'','#'+(i+1));}}
function avancar(){{if(passo<passos[i].length)revelar(i,++passo);else if(i<frames.length-1)show(i+1);}}
function voltar(){{if(passo>0)revelar(i,--passo);else if(i>0)show(i-1,true);}}
addEventListener('resize',fit);
addEventListener('keydown',e=>{{if(['ArrowRight','PageDown',' '].includes(e.key))avancar();
  else if(['ArrowLeft','PageUp'].includes(e.key))voltar();
  else if(e.key==='n'||e.key==='N')document.body.classList.toggle('show-notes');
  else if(e.key==='f'||e.key==='F')document.documentElement.requestFullscreen?.();}});
addEventListener('click',e=>e.clientX>innerWidth/2?avancar():voltar());
fit();show((parseInt(location.hash.slice(1))||1)-1);
</script></body></html>"""
out = deck_dir / "apresentacao.html"
out.write_text(page, encoding="utf-8")
print(f"{out} ({len(deck['order'])} slides)")
