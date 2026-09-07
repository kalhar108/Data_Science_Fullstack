
from pathlib import Path
import ast, sys
root=Path(__file__).parent
apps=sorted(root.glob('[0-9][0-9]_*/app.py'))
assert len(apps)==16, f'Expected 16 apps, got {len(apps)}'
failed=[]
for p in apps:
    try: ast.parse(p.read_text())
    except Exception as e: failed.append((str(p),str(e)))
if failed:
    print(failed); sys.exit(1)
for req in ['README.md','PROMPTS.md','EXPERIMENT_NOTES.md','VIDEO_WALKTHROUGH_SCRIPT.md','requirements.txt']:
    assert (root/req).exists(), req
print('OK: 16 app.py files parse successfully and required artifacts are present.')
