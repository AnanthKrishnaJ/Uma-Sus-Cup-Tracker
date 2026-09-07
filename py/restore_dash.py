with open('old_index.html', 'r', encoding='utf-16') as f:
    old_html = f.read()

html_start = old_html.find('<!-- DASHBOARD VIEW -->')
html_end = old_html.find('<!-- SUS CUP HISTORY VIEW -->')
old_dash_html = old_html[html_start:html_end]

js_start = old_html.find('renderDashboard() {')
js_end = old_html.find('renderHistory() {')
old_dash_js = old_html[js_start:js_end]

with open('index.html', 'r', encoding='utf-8') as f:
    curr_html = f.read()

curr_html_start = curr_html.find('<!-- DASHBOARD VIEW -->')
curr_html_end = curr_html.find('<!-- SUS CUP HISTORY VIEW -->')
curr_html = curr_html[:curr_html_start] + old_dash_html + curr_html[curr_html_end:]

curr_js_start = curr_html.find('renderDashboard() {')
curr_js_end = curr_html.find('renderHistory() {')
curr_html = curr_html[:curr_js_start] + old_dash_js + curr_html[curr_js_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(curr_html)

print('Restored old dashboard and JS.')
