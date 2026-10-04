"""One issue per release; retry/force updates its body, without extra comments."""
import json, os, urllib.request
from pathlib import Path
from check import api, pages
repo = os.environ['GH_REPO']; tag = os.environ['TAG']
marker = f'<!-- dnd5e-compatibility:{tag} -->'
body = marker + '\n' + Path(os.environ['REPORT']).read_text()
if len(body) > 60000:
    body = marker + '\nInforme demasiado extenso: consulte el archivo ' + os.environ['REPORT'] + ' en el repositorio y el artefacto de Actions.'
existing = next((i for i in pages(f'repos/{repo}/issues') if marker in (i.get('body') or '') and 'pull_request' not in i), None)
# Include closed issues as well to keep forced runs idempotent.
if existing is None:
    for page in range(1, 100):
        batch = api(f'repos/{repo}/issues?state=closed&per_page=100&page={page}')
        existing = next((i for i in batch if marker in (i.get('body') or '') and 'pull_request' not in i), None)
        if existing or len(batch)<100: break
path = f'repos/{repo}/issues' + (f'/{existing["number"]}' if existing else '')
request = urllib.request.Request('https://api.github.com/'+path,
    data=json.dumps({'title':f'Informe de compatibilidad DND5e — {tag}', 'body':body}).encode(),
    headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'], 'Accept':'application/vnd.github+json', 'User-Agent':'dnd5e-compatibility-checker'},
    method='PATCH' if existing else 'POST')
with urllib.request.urlopen(request, timeout=60) as response: print(json.load(response)['html_url'])
