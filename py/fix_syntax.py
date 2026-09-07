import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the start
content = content.replace(
    "            },\n        // CSS for Compare Redesign (Injected dynamically)\n        if (!document.getElementById('compare-styles')) {",
    "            },\n            renderCompare() {\n        // CSS for Compare Redesign (Injected dynamically)\n        if (!document.getElementById('compare-styles')) {"
)

# Fix the end
content = content.replace(
    "            });\n        }\n    }\n\n\n            \n            renderProfileView() {",
    "            });\n        }\n    },\n\n\n            \n            renderProfileView() {"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
