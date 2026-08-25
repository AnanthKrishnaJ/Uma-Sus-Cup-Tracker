import re, json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace specific gametora urls that are missing IDs
corrections = {
    'https://gametora.com/umamusume/characters/gold-ship': 'https://gametora.com/umamusume/characters/100101-gold-ship',
    'https://gametora.com/umamusume/characters/mejiro-mcqueen': 'https://gametora.com/umamusume/characters/101301-mejiro-mcqueen',
    'https://gametora.com/umamusume/characters/symboli-rudolf': 'https://gametora.com/umamusume/characters/101701-symboli-rudolf',
    'https://gametora.com/umamusume/characters/mayano-top-gun': 'https://gametora.com/umamusume/characters/102401-mayano-top-gun',
    'https://gametora.com/umamusume/characters/tokai-teio': 'https://gametora.com/umamusume/characters/100301-tokai-teio',
    'https://gametora.com/umamusume/characters/oguri-cap': 'https://gametora.com/umamusume/characters/100601-oguri-cap',
    'https://gametora.com/umamusume/characters/agnes-tachyon': 'https://gametora.com/umamusume/characters/103201-agnes-tachyon',
    'https://gametora.com/umamusume/characters/super-creek': 'https://gametora.com/umamusume/characters/104501-super-creek',
    'https://gametora.com/umamusume/characters/seiun-sky': 'https://gametora.com/umamusume/characters/102001-seiun-sky',
    'https://gametora.com/umamusume/characters/grass-wonder': 'https://gametora.com/umamusume/characters/101101-grass-wonder',
    'https://gametora.com/umamusume/characters/narita-taishin': 'https://gametora.com/umamusume/characters/103301-narita-taishin',
    'https://gametora.com/umamusume/characters/taiki-shuttle': 'https://gametora.com/umamusume/characters/101001-taiki-shuttle',
    'https://gametora.com/umamusume/characters/el-condor-pasa': 'https://gametora.com/umamusume/characters/101401-el-condor-pasa',
    'https://gametora.com/umamusume/characters/haru-urara': 'https://gametora.com/umamusume/characters/105201-haru-urara',
    'https://gametora.com/umamusume/characters/tm-opera-o': 'https://gametora.com/umamusume/characters/101501-tm-opera-o',
    'https://gametora.com/umamusume/characters/t.m.-opera-o': 'https://gametora.com/umamusume/characters/101501-tm-opera-o',
    'https://gametora.com/umamusume/characters/mihono-bourbon': 'https://gametora.com/umamusume/characters/102601-mihono-bourbon',
    'https://gametora.com/umamusume/characters/sakura-bakushin-o': 'https://gametora.com/umamusume/characters/105301-sakura-bakushin-o',
    'https://gametora.com/umamusume/characters/daiwa-scarlet': 'https://gametora.com/umamusume/characters/100901-daiwa-scarlet',
    'https://gametora.com/umamusume/characters/maruzensky': 'https://gametora.com/umamusume/characters/100401-maruzensky',
    'https://gametora.com/umamusume/characters/smart-falcon': 'https://gametora.com/umamusume/characters/104601-smart-falcon'
}

count = 0
for bad, good in corrections.items():
    text, n = re.subn(f'"{bad}"', f'"{good}"', text)
    count += n

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Replaced {count} bad URLs.')
