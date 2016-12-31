import bs4 as bs
import pandas as pd
import urllib.request

# sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
sauce = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
soup = bs.BeautifulSoup(sauce, "lxml")

"""
table = soup.find("table")

table_rows = table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text for i in td]
    print(row)

# Using Pandas
dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/", header=0)
for df in dfs:
    print(df)
"""

for url in soup.find_all("loc"):
    print(url.text)
