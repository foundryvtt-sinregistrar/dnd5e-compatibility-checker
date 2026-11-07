import sys, tempfile, json, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from check import within, load, safe_path, audit, markdown
class Checks(unittest.TestCase):
    def test_ranges(self):
        self.assertTrue(within('14.370', {'minimum':'14'}))
        self.assertFalse(within('6.1.0', {'maximum':'6.0.5'}))
        self.assertFalse(within('6.0.2', {'minimum':'6.0.3'}))
    def test_duplicate_and_escape(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); p=root/'x.json'; p.write_text('{"a":1,"a":2}')
            with self.assertRaises(ValueError): load(p)
            with self.assertRaises(ValueError): safe_path(root, '../outside')
    def test_missing_invalid_and_runtime(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'module.json').write_text(json.dumps({'id':'x','compatibility':{'verified':'14.370'},'relationships':{'systems':[{'id':'dnd5e','compatibility':{'maximum':'6.0.4'}}]},'esmodules':['missing.js']}))
            (root/'bad.json').write_text('{')
            result=audit(root,'6.0.5','14.370',root)
            self.assertEqual(result['status'],'ERROR')
            self.assertTrue({'VERSION_RANGE','JSON_INVALID','MISSING_FILE'} <= {f['code'] for f in result['findings']})
    def test_syntax_and_babele_not_green(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'module.json').write_text(json.dumps({'id':'x','compatibility':{'verified':'14.370'},'relationships':{'systems':[{'id':'dnd5e','compatibility':{'verified':'6.0.5'}}],'requires':[{'id':'babele'}]},'esmodules':['ok.js']}))
            (root/'ok.js').write_text('export const x = 1;')
            (root/'imported.js').write_text('export const converter = () => {};')
            self.assertEqual(audit(root,'6.0.5','14.370',root)['status'],'REVISAR')
            (root/'ok.js').write_text('export const = ;')
            self.assertEqual(audit(root,'6.0.5','14.370',root)['status'],'ERROR')
    def test_removed_key_and_path(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); mod=root/'mod'; old=root/'old'; new=root/'new'
            mod.mkdir(); (old/'lang').mkdir(parents=True); (new/'lang').mkdir(parents=True)
            (old/'lang/en.json').write_text('{"DND5E":{"Removed":"old"}}')
            (new/'lang/en.json').write_text('{"DND5E":{"Added":"new"}}')
            (mod/'module.json').write_text(json.dumps({'compatibility':{'verified':'14.370'},'relationships':{'systems':[{'id':'dnd5e','compatibility':{'verified':'6.0.5'}}]},'esmodules':['main.js']}))
            (mod/'main.js').write_text('const key = "DND5E.Removed"; const path = "systems/dnd5e/templates/missing.hbs";')
            result=audit(mod,'6.0.5','14.370',new,old)
            self.assertTrue({'REMOVED_I18N','UPSTREAM_PATH'} <= {f['code'] for f in result['findings']})
    def test_documentation_conventions(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); upstream=root/'upstream'; (upstream/'lang').mkdir(parents=True)
            (upstream/'lang/en.json').write_text('{"DND5E":{}}')
            (root/'module.json').write_text(json.dumps({'id':'example-module','compatibility':{'verified':'14.370'},'relationships':{'systems':[{'id':'dnd5e','compatibility':{'verified':'6.0.5'}}]}}))
            result=audit(root,'6.0.5','14.370',upstream)
            codes={f['code'] for f in result['findings']}
            self.assertTrue({'README_ES_MISSING','README_EN_MISSING','CHANGELOG_MISSING'} <= codes)
            (root/'README.md').write_text('[English](README.en.md)\nhttps://github.com/foundryvtt-sinregistrar/example-module/releases/latest/download/module.json\n', encoding='utf-8')
            (root/'README.en.md').write_text('[Español](README.md)\nhttps://github.com/foundryvtt-sinregistrar/example-module/releases/latest/download/module.json\n', encoding='utf-8')
            (root/'CHANGELOG.md').write_text('# Changelog\n\n## [Unreleased]\n\n## [1.0.0] - 2026-10-29\n\n### Added\n\n- First release.\n', encoding='utf-8')
            result=audit(root,'6.0.5','14.370',upstream)
            codes={f['code'] for f in result['findings']}
            self.assertFalse(any(code.startswith('README_') or code.startswith('CHANGELOG_') for code in codes), codes)
if __name__=='__main__': unittest.main()
