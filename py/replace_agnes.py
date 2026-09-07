import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('"player": "agnes"', '"player": "Agnes"')
        content = content.replace('"trainer": "agnes"', '"trainer": "Agnes"')

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
