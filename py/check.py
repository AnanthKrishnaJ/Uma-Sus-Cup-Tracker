with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('showRaceDetail')
end_idx = html.find('renderPlayers() {', idx)
print(html[idx:end_idx])
