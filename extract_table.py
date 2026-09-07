import json
import codecs

with codecs.open('full_table.txt', 'w', encoding='utf-8') as f:
    for line in open(r'c:\Users\anant\.gemini\antigravity-ide\brain\a367841e-7315-4742-a588-3b0cfd74eb26\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8'):
        d = json.loads(line)
        if d.get('type') == 'USER_INPUT' and 'suscup 26 missing values' in d.get('content', ''):
            f.write(d['content'])
