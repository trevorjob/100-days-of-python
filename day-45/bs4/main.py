from bs4 import BeautifulSoup
import lxml

import requests

response = requests.get('https://news.ycombinator.com/')
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
article_tag =soup.find_all(name='span', class_='titleline')
up_vote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
art_text = []
art_link = []
for art in article_tag:
    att = art.getText()
    art_text.append(att)
    att = art.select_one('a').get('href')
    art_link.append(att)

# up_ints = [up[0].split()[0] for up in up_vote]
# print(soup.title)
# print(soup.select_one(".titleline a"))
# print(soup.select(".titleline a"))
# print(article_tag)
print(up_vote)
# print(art_link)
# print(art_text)

higest_ind = up_vote.index(max(up_vote))

g = art_text.index(art_text[higest_ind])
print(up_vote[g])
print(art_link[higest_ind])
print(art_text[higest_ind])
print(higest_ind, max(up_vote))



















# with open("web.html", encoding='utf8') as file:
#         content = file.read()


# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title.name)
# # print(soup.title.string)

# anchor_tags = soup.find_all(name="a")
# for tag in anchor_tags:
#         # print(tag.getText())
#         print(tag.get("href"))

# heading = soup.find(name="h1", id='name')
# print(heading)

# section_heading = soup.find(name='h3', class_='heading')

# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)






