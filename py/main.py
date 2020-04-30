import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://www.tecmundo.com.br/blog/novidades")

res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find(class_="tec--btn").find_all

all_pages = []
for link in links:
    page = requests.get(link.get('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))

print(len(all_pages))


all_post = []
for posts in all_pages:
    posts = posts.find_all(class_="tec--list__item")
    for post in posts:        
        info = post.find(class_="tec--card")
        title = info.h3.text
        preview = info.p.text
        author = info.find(class_="post-author").text
        time = info.find(class_="tec--timestamp__item")
        img = info.find(class_="tec--card__thumb__link")
        all_post.append({
            'title': title,
            'date': time        
        })
print (all_post)
with open('posts.json', 'w') as json_file:
    json.dump(all_post, json_file, indent=3) #ensure_ascii="false"