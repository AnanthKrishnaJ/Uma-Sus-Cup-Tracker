import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the JSON error by extracting the correct JSON string
# Using a custom parser or just searching up to "winners": [
start_idx = text.find('const INITIAL_DATA = {')
end_idx = text.find('};\n\nconst PREDETERMINED_COLORS')
if end_idx == -1:
    end_idx = text.find('};\nconst PREDETERMINED_COLORS')
if end_idx == -1:
    print("Cannot find end of INITIAL_DATA")
else:
    json_str = text[start_idx + 21:end_idx + 1]
    import json
    try:
        json.loads(json_str)
        print("JSON is valid!")
    except json.JSONDecodeError as e:
        print(f"JSON error at {e.lineno}:{e.colno} - {e.msg}")
        start_err = max(0, e.pos - 50)
        end_err = min(len(json_str), e.pos + 50)
        print("Context:")
        print(json_str[start_err:end_err])
