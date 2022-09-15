'''

Pega todos os links do site da variável url e salva em um arquivo

'''

import requests
import re
urls = set()
url = 'https://www.globo.com/'
r = requests.get(url)
html = r.text
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html)
f = open("urls.txt", "w")
for link in search:
    if link not in urls:
        urls.add(link)
        f.write(f"{link}\n")

f.close()