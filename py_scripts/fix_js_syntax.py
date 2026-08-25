with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''                    }
                        <div style="margin-top:12px;">${winnersHtml}</div>'''

replacement = '''                    }
                    return `<div class="timeline-item"><div class="card" style="margin-bottom:0; cursor:pointer;" onclick="App.showRaceDetail(${race.id})">
                        <span class="badge" style="background:var(--accent-dark);">SUS CUP ${race.cupNumber}</span>
                        <h3 style="font-size:1.35rem; margin:12px 0 5px;">${race.name}</h3>
                        <p style="color:var(--text-muted); font-weight:700;">${race.date}  ${race.course} ${race.distance}m ${race.surface}</p>
                        <div style="margin-top:12px;">${winnersHtml}</div>'''

if target in text:
    text = text.replace(target, replacement)
    with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Fixed JS syntax error!')
else:
    print('Target not found!')
