import os
import sys
import subprocess

scripts = [
    'update_cups.py',
    'update_names.py',
    'replace.py',
    'replace2.py',
    'replace_agnes.py',
    'patch_21.py',
    'patch_22_23.py',
    'patch_24_25.py',
    'add_winners.py',
    'patch_21_winners.py',
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run([sys.executable, script], check=True)
print("Restoration complete!")
