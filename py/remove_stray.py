import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('App.renderDashboard = function() {')
if idx != -1:
    end_idx = html.find('App.init();', idx)
    if end_idx != -1:
        # Just to be safe, find the exact function block end
        new_html = html[:idx] + html[end_idx:]
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Removed stray renderDashboard at the bottom.")
