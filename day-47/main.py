import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Write your code below this line 👇


response = requests.get(url=URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"})
page = response.text

soup = BeautifulSoup(page, "html.parser")
bb = soup.find(name='span', class_='a-offscreen')
print(bb.get_text())
# print(bb)