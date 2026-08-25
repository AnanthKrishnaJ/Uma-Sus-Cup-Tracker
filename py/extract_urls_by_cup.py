import json
import re

transcript_path = r"C:\Users\anant\.gemini\antigravity-ide\brain\699bfb4f-b87d-4760-8352-6340064600b4\.system_generated\logs\transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                content = data.get('content', '')
                if 'discord.com' in content:
                    match = re.search(r'SUS CUP \d+', content)
                    cup_name = match.group(0) if match else "UNKNOWN"
                    urls = re.findall(r'https?://discord.com/[^\s"\'\\]+', content)
                    print(f"--- {cup_name} ---")
                    for u in urls:
                        print(u)
        except:
            pass
