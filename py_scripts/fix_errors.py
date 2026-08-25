import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix escaped quotes in DOMContentLoaded
html = html.replace(r"document.addEventListener(\'DOMContentLoaded\', () => { App.init(); });", 
                    "document.addEventListener('DOMContentLoaded', () => { App.init(); });")
# Also just in case there are others
html = html.replace(r"\'DOMContentLoaded\'", "'DOMContentLoaded'")

# 2. Extract the corrupted NPC lines at the end of the file
corrupted_pattern = r'</html\s*(,\s*"Ogress"[\s\S]*?)>'
match = re.search(corrupted_pattern, html)
if match:
    npc_data = match.group(1)
    # Remove it from the end of the file
    html = re.sub(corrupted_pattern, '</html>', html)
    
    # Insert it into UMA_DATABASE
    # Find the end of UMA_DATABASE
    db_pattern = r'(const UMA_DATABASE = \{)([\s\S]*?)(\s*\};)'
    db_match = re.search(db_pattern, html)
    if db_match:
        new_db = db_match.group(1) + npc_data + "," + db_match.group(2) + db_match.group(3)
        html = html[:db_match.start()] + new_db + html[db_match.end():]
        print("Fixed corrupted NPC data at the end of the file.")
else:
    print("Corrupted NPC data not found at the end of the file.")

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixes applied.")
