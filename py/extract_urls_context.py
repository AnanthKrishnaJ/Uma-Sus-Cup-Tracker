import json
import re

transcript_path = r"C:\Users\anant\.gemini\antigravity-ide\brain\699bfb4f-b87d-4760-8352-6340064600b4\.system_generated\logs\transcript_full.jsonl"

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                content = data.get('content', '')
                if 'discord.com/channels' in content:
                    print("USER PROMPT CONTAINING DISCORD URL:\n", content[:500], "...\n")
        except:
            pass
