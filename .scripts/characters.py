import urllib.request
from bs4 import BeautifulSoup

url_main = 'http://shakespeare.mit.edu/'
pagesource_main = urllib.request.urlopen(url_main)
menu = BeautifulSoup(pagesource_main, 'html.parser')
urls = []
for tag in menu.find_all('a'):
    if 'index.html' in tag.get('href'):
        path = tag.get('href')
        link = url_main + path.replace('index','full')
        urls.append(link)

name_attr = []
for i in range(406):
    name_attr.append('speech%s' % (i+1))
characters = []
i=0
for url in urls:
    i+=1
    pagesource = urllib.request.urlopen(url)
    content = BeautifulSoup(pagesource, 'html.parser')
    for valid_attr in name_attr:
        tags = content.find_all('a', {'name':valid_attr})
        if tags == []:
            break
        for tag in tags:
            character = tag.string
            characters.append(character)
            characters = list(set(characters))

non_characters = ['Scene III', '& C', 'SU FFOLK', 'As long as you or I', 'Here stand I', 'This way will I', 'Posthumus Leonatus', 'ALL', 'BOTH', 'All', 'Both', 'Some Others', 'Some Speak']
for non_character in non_characters:
    if non_character in characters:
        characters.remove(non_character)
repeats = ['A ', 'All The ', 'All the ', 'All ', 'Both ', 'Several ', 'First ', 'Second ', 'Third ', 'Fourth ', 'Fifth ', 'Sixth ', 'Seventh ']
for repeat in repeats:
    for i in range(len(characters)):
        if repeat in characters[i]:
            characters[i] = characters[i].replace(repeat, '')
            if characters[i] == characters[i].lower():
                characters[i] = characters[i][0].upper() + characters[i][1:]
characters = list(set(characters))

main_characters = []
minor_characters = []
for character in characters:
    if character == character.upper() or 'Ghost of' in character or 'Young' in character:
        main_characters.append(character)
    else:
        minor_characters.append(character)
main_characters.sort()
minor_characters.sort()

f=open('../include/characters.wordlist','w+')
for character in main_characters:
    f.write(character + '\n')
f.write('\n')
for character in minor_characters:
    f.write(character + '\n')
f.close()
