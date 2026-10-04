#!/usr/bin/env python3
"""Read-only static audit. Never imports or executes downloaded module code."""
import argparse, datetime, json, os, re, subprocess, tempfile, urllib.request
from pathlib import Path

API = 'https://api.github.com/'

def api(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'dnd5e-compatibility-checker'}
    if os.environ.get('GH_TOKEN'): headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    with urllib.request.urlopen(urllib.request.Request(API + path, headers=headers), timeout=60) as response:
        return json.load(response)

def pages(path):
    result = []
    for page in range(1, 100):
        batch = api(f'{path}?per_page=100&page={page}')
        result.extend(batch)
        if len(batch) < 100: return result
    raise RuntimeError('Pagination limit exceeded')

def clone(repo, ref, destination):
    subprocess.run(['git', '-c', 'advice.detachedHead=false', 'clone', '--quiet', '--depth=1', '--branch', ref,
                    f'https://github.com/{repo}.git', str(destination)], check=True, timeout=300)
    return subprocess.check_output(['git', '-C', str(destination), 'rev-parse', 'HEAD'], text=True).strip()

def load(path):
    def unique(pairs):
        out = {}
        for k, v in pairs:
            if k in out: raise ValueError(f'Duplicate key: {k}')
            out[k] = v
        return out
    return json.loads(path.read_text(encoding='utf-8-sig'), object_pairs_hook=unique)

def version(value):
    if not re.fullmatch(r'\d+(?:\.\d+){0,3}', str(value)): raise ValueError(f'Unsupported version: {value}')
    parts = tuple(map(int, str(value).split('.')))
    return parts + (0,) * (4-len(parts))

def within(target, bounds):
    for key, operator in [('minimum', lambda a,b:a<b), ('maximum', lambda a,b:a>b)]:
        if bounds.get(key) and operator(version(target), version(bounds[key])): return False
    return True

def safe_path(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()): raise ValueError('Path outside module')
    return path

def flatten(data, prefix=''):
    result = set()
    if isinstance(data, dict):
        for key, value in data.items(): result |= flatten(value, f'{prefix}.{key}' if prefix else key)
    else: result.add(prefix)
    return result

def audit(root, target, foundry, upstream, old=None):
    findings = []
    def add(level, code, text): findings.append({'level':level, 'code':code, 'message':text})
    manifest = load(root / 'module.json')
    systems = manifest.get('relationships', {}).get('systems', [])
    system = next((s for s in systems if s.get('id') == 'dnd5e'), None)
    if system is None: add('review', 'SYSTEM_UNDECLARED', 'No declara relationships.systems.dnd5e')
    for name, bounds, current in [('Foundry', manifest.get('compatibility', {}), foundry),
                                  ('DND5e', (system or {}).get('compatibility', {}), target)]:
        if not within(current, bounds): add('error', 'VERSION_RANGE', f'{name} {current} fuera del rango declarado {bounds}')
        if not bounds.get('verified') or version(current) > version(bounds['verified']):
            add('review', 'UNVERIFIED', f'{name} {current}: verificación declarada {bounds.get("verified", "ausente")}')
    files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and not p.is_symlink()]
    for path in files:
        if path.suffix == '.json':
            try: load(path)
            except (ValueError, UnicodeError) as exc: add('error', 'JSON_INVALID', f'{path.relative_to(root)}: {exc}')
    declared = manifest.get('scripts', []) + manifest.get('esmodules', []) + manifest.get('styles', [])
    declared += [x['path'] for x in manifest.get('languages', [])]
    declared += [x['path'] for x in manifest.get('packs', [])]
    for name in declared:
        if not safe_path(root, name).exists(): add('error', 'MISSING_FILE', f'Archivo declarado ausente: {name}')
    js = [p for p in files if p.suffix in ('.js', '.mjs')]
    for path in js:
        relative = str(path.relative_to(root))
        text = path.read_text(encoding='utf-8-sig')
        # Both classic scripts and modules are syntax-checked without execution.
        checked = subprocess.run(['node', '--input-type=commonjs' if relative in manifest.get('scripts', []) else '--input-type=module', '--check'], input=text, text=True, capture_output=True)
        if checked.returncode: add('error', 'JS_SYNTAX', f'{relative}: {checked.stderr[:500]}')
        for name in sorted(set(re.findall(r'systems/dnd5e/([\w./-]+\.(?:hbs|html|js|mjs|json))', text))):
            if not safe_path(upstream, name).exists(): add('review', 'UPSTREAM_PATH', f'{relative}: ruta no encontrada systems/dnd5e/{name}')
        if old:
            keys = set(re.findall(r'[\"\'](DND5E\.[\w.]+)[\"\']', text))
            old_keys = flatten(load(old/'lang/en.json'))
            new_keys = flatten(load(upstream/'lang/en.json'))
            for key in sorted(keys & (old_keys-new_keys)): add('review', 'REMOVED_I18N', f'{relative}: clave eliminada {key}')
    requires = manifest.get('relationships', {}).get('requires', [])
    babele = any(x.get('id') == 'babele' for x in requires)
    if babele: add('review', 'BABELE_COVERAGE', 'JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele')
    if js: add('review', 'RUNTIME_PENDING', 'Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry')
    if manifest.get('packs'): add('review', 'PACK_RUNTIME', 'Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry')
    external = [x['id'] for x in requires if x.get('id') != 'babele']
    if external: add('review', 'DEPENDENCIES', 'Dependencias no instaladas en esta auditoría: ' + ', '.join(external))
    status = 'ERROR' if any(f['level']=='error' for f in findings) else 'REVISAR' if findings else 'PASS ESTÁTICO'
    return {'id':manifest.get('id'), 'type':'Babele + JavaScript' if babele else 'JavaScript/compendios', 'status':status, 'findings':findings}

def markdown(report):
    lines = [f'# Informe DND5e — {report["tag"]}', '', f'Fecha UTC: {report["date"]}',
             f'Foundry objetivo: {report["foundry"]}', f'Comparación: {report.get("previous") or "sin línea base"} → {report["tag"]}',
             '', 'Auditoría estática: PASS no acredita compatibilidad funcional. ERROR indica fallo de datos/rango; REVISAR requiere comprobación humana.',
             '', '| Repositorio | Estado | Tipo | Commit |', '|---|---|---|---|']
    for r in report['modules']: lines.append(f'| {r["repo"]} | {r["status"]} | {r.get("type", "desconocido")} | {r.get("sha", "")[:12]} |')
    for r in report['modules']:
        lines += ['', f'## {r["repo"]}']
        for f in r['findings']: lines.append(f'- **{f["code"]}**: ' + f['message'].replace('\n', ' ').replace('`', "'"))
        lines += ['- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.']
    lines += ['', '## Límites', 'No se ejecuta código de terceros. No se cargan Foundry, Babele ni contenido comercial. No se demuestra cobertura de traducciones sin compendios fuente. Los repositorios se auditan en HEAD de su rama por defecto; no necesariamente coinciden con el ZIP publicado.']
    return '\n'.join(lines)+'\n'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config/settings.json'); parser.add_argument('--force', action='store_true')
    args = parser.parse_args(); config = load(Path(args.config))
    release = api(f'repos/{config["upstream"]}/releases/latest')
    tag = release['tag_name']; target = tag.removeprefix('release-')
    version(target)
    reports = Path('reports'); reports.mkdir(exist_ok=True)
    state_path = reports/'state.json'; state = load(state_path) if state_path.exists() else {}
    if state.get('tag') == tag and not args.force:
        print('Sin nueva release'); return
    previous = state.get('tag')
    report = {'tag':tag, 'previous':previous, 'date':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'foundry':config['foundry_version'], 'release_url':release['html_url'], 'modules':[]}
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp); upstream = temp/'upstream'; report['upstream_sha'] = clone(config['upstream'], tag, upstream)
        old = None
        if previous and previous != tag:
            old = temp/'old'; clone(config['upstream'], previous, old)
        for repo in pages(f'users/{config["owner"]}/repos'):
            if repo['archived'] or repo['name'] in config['exclude']: continue
            row = {'repo':repo['full_name']}
            try:
                root = temp/repo['name']; row['sha'] = clone(repo['full_name'], repo['default_branch'], root)
                if not (root/'module.json').exists():
                    row.update(status='NO APLICA', findings=[{'code':'NO_MANIFEST','message':'Sin module.json en raíz', 'level':'info'}])
                else: row.update(audit(root, target, config['foundry_version'], upstream, old))
            except Exception as exc: row.update(status='ERROR DE AUDITORÍA', findings=[{'code':'AUDIT_FAILED','message':str(exc), 'level':'error'}])
            report['modules'].append(row)
    stem = f'dnd5e-{target}'
    (reports/f'{stem}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    (reports/f'{stem}.md').write_text(markdown(report))
    failed = any(r['status']=='ERROR DE AUDITORÍA' for r in report['modules'])
    if not failed: state_path.write_text(json.dumps({'tag':tag})+'\n')
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'],'a') as out: out.write(f'changed=true\nreport=reports/{stem}.md\ntag={tag}\naudit_failed={str(failed).lower()}\n')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as out: out.write(markdown(report))
    print(markdown(report))
    return 2 if failed else 0

if __name__ == '__main__': raise SystemExit(main())
