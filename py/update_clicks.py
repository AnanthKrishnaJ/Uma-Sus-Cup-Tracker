import re

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make player names clickable in the player leaderboard
# Find the specific div for players which has the avatar-circle next to it
replacement = """<div style="display:flex; align-items:center; gap:10px; cursor:pointer;" onclick="App.showTrainerProfile('${player.name}')" title="View Trainer Profile">"""

content = content.replace(
    '<div style="display:flex; align-items:center; gap:10px;">\n                                <div class="avatar-circle">',
    replacement + '\n                                <div class="avatar-circle">'
)

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated click handler.")
