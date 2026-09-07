
import subprocess,sys
from pathlib import Path
projects=sorted([p for p in Path('.').iterdir() if p.is_dir() and p.name[:2].isdigit()])
for i,p in enumerate(projects): print(f"{i:2}: {p.name}")
choice=int(input("Project number: "))
subprocess.run([sys.executable,"-m","streamlit","run",str(projects[choice]/"app.py")])
