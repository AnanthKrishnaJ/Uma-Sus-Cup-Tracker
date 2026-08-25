import json
import os

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

updated = False
for race in data['races']:
    cup_id = race.get('id')
    if cup_id and cup_id >= 21 and cup_id <= 24: # Assuming 25,26 aren't in tracker yet
        # check if it has the right images
        expected_images = []
        for i in range(1, 5):
            filename = f"{cup_id}.{i}.png"
            # check if file exists in the directory
            file_path = os.path.join('../.vscode/suscupimages21-30', filename)
            if os.path.exists(file_path):
                expected_images.append(f"suscupimages21-30/{filename}")
        
        # update race images
        if race.get('images') != expected_images:
            race['images'] = expected_images
            updated = True

if updated:
    new_json = json.dumps(data, indent=4)
    content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Images linked for cups 21-24!")
else:
    print("No updates needed.")
