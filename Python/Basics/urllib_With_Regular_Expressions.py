import urllib.request
import urllib.parse
import re

url = "http://pythonprogramming.net"
values = {"s": "basics", "submit": "search"}
data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)

paragraphs = re.findall(r"<p>(.*?)</p>", str(resp_data))

for p in paragraphs:
    print(p)
