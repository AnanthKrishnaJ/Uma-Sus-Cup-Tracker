import os
import sys
import subprocess
import re

scripts = [
    'patch_21.py',
    'patch_22_23.py',
    'patch_24_25.py',
    'patch_26.py',
    'add_winners.py',
    'patch_21_winners.py',
]

for script in scripts:
    print(f"Running {script}...")
    try:
        subprocess.run([sys.executable, script], check=True)
    except Exception as e:
        print(f"Failed to run {script}")

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Agnes with agnes
text = text.replace('"player": "Agnes"', '"player": "agnes"')
text = text.replace('"player": "agnes "', '"player": "agnes"')
text = text.replace('"player": " Agnes"', '"player": "agnes"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restoration complete 2!")
