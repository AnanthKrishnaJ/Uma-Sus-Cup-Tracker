import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = """
                    .champ-history-container {
                        width: 100%;
                        background: #ffffff;
                        border-radius: var(--radius-lg);
                        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
                        border: 1px solid var(--border-color);
                        overflow: hidden;
                    }
                    .champ-row {
                        display: grid;
                        grid-template-columns: 1.2fr 1fr 1.8fr;
                        align-items: center;
                        padding: 16px 20px;
                        border-bottom: 1px solid var(--glass-border);
                        transition: all 0.2s ease;
                    }
                    .champ-row:last-child {
                        border-bottom: none;
                    }
                    .champ-row:hover {
                        background: rgba(0,0,0,0.015);
                        transform: translateX(2px);
                    }
                    .champ-header {
                        display: grid;
                        grid-template-columns: 1.2fr 1fr 1.8fr;
                        text-transform: uppercase;
                        font-size: 0.75rem;
                        letter-spacing: 1.5px;
                        color: var(--text-muted);
                        font-weight: 800;
                        background: var(--bg-color);
                        border-bottom: 2px solid var(--border-color);
                        padding: 15px 20px;
                    }
"""

content = re.sub(
    r'\.champ-history-container\s*\{[\s\S]*?padding:\s*10px\s+15px;\s*\}',
    new_css.strip(),
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Championship History CSS")
