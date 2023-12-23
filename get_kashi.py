import bs4
import requests

res = requests.get("https://www.uta-net.com/song/122749/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.find(id="kashi_area")
for elem in elems:
    if len(elem.text) == 0:
        continue
    print(elem.text)
