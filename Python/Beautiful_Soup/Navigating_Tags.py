# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
soup = bs.BeautifulSoup(sauce, "lxml")

nav = soup.nav
for url in nav.find_all("a"):
    print(url.get("href"))

body = soup.body
for paragraph in body.find_all("p"):
    print(paragraph.text)

for div in soup.find_all("div", class_="body"):
    print(div.text)
