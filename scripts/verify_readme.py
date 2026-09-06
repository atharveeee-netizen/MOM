import os, re

content = open('README.md', encoding='utf-8').read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
imgs += re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)

print('--- CHECKING IMAGES ---')
all_ok = True
for img in set(imgs):
    if img.startswith('http'):
        print('HTTP image:', img)
    else:
        exists = os.path.exists(img)
        print(f'{img}: {"EXISTS" if exists else "MISSING"}')
        if not exists:
            all_ok = False

print('\n--- CHECKING LOCAL FILE LINKS ---')
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', content)
for l in set(links):
    if not l.startswith('http') and not l.startswith('#'):
        exists = os.path.exists(l)
        print(f'{l}: {"EXISTS" if exists else "MISSING"}')
        if not exists:
            all_ok = False

if all_ok:
    print('\nALL IMAGES AND LINKS VERIFIED PERFECTLY!')
else:
    print('\nWARNING: SOME LINKS ARE BROKEN!')
