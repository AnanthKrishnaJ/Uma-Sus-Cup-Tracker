import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix space issue on left
content = content.replace(
    '.sidebar {\n            width: 280px;\n            background: #111111;\n            position: fixed;\n            height: 100vh;',
    '.sidebar {\n            width: 280px;\n            background: #111111;\n            position: fixed;\n            left: 0;\n            top: 0;\n            height: 100vh;'
)

# Rename Hall of Fame to Player Profiles in sidebar
content = content.replace(
    '<li><a href="#" data-nav="players"><i class="fa-solid fa-medal"></i> <span>Hall of Fame</span></a></li>',
    '<li><a href="#" data-nav="players"><i class="fa-solid fa-user-group"></i> <span>Player Profiles</span></a></li>'
)

# Also rename the header inside the view-players view
content = content.replace(
    '<h2>Leaderboard</h2>\n                <p>Overall player standings</p>',
    '<h2>Player Profiles</h2>\n                <p>Overall player standings & profiles</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Changes applied!")
