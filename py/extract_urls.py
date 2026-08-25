import json
import re

transcript_path = r"C:\Users\anant\.gemini\antigravity-ide\brain\699bfb4f-b87d-4760-8352-6340064600b4\.system_generated\logs\transcript_full.jsonl"
urls = set()

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                content = data.get('content', '')
                found = re.findall(r'https?://[^\s"\'\\]+', content)
                for url in found:
                    urls.add(url)
        except:
            pass

print("User provided URLs:")
for u in urls:
    print(u)
