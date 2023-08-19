import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
page = response.text

soup = BeautifulSoup(page, "html.parser")
names = [n.getText()+ '\n' for n in soup.find_all(name='h3', class_='title')]
with open('movies.txt', 'w', encoding='utf-8') as f:
    for name in names[::-1]:
        f.write(name)


