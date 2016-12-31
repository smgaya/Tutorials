# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
soup = bs.BeautifulSoup(sauce, "lxml")

# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.find_all("p"))

for paragraph in soup.find_all("p"):
    print(paragraph.text)

# print(soup.get_text)

for url in soup.find_all("a"):
    print(url.get("href"))
