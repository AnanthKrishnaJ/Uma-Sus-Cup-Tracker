with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('showRaceDetail(raceId)')
end = text.find('},', start)
print(text[end-800:end+50].encode('ascii', 'ignore').decode('ascii'))
