# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import urllib.request
import urllib.parse

'''
url = "http://pythonprogramming.net"

values = {"s": "basic", "submit": "search"}

data = urllib.parse.urlencode(values)
data = data.encode(encoding="utf-8")
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
'''

try:
    x = urllib.request.urlopen("https://www.google.com/search?q=test")
    print(x.read())
except Exception as ex:
    print(ex)

try:
    url = "https://www.google.com/search?q=test"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()

    save_file = open("urllib_headers.txt", "w")
    save_file.write(str(resp_data))
    save_file.close()
except Exception as ex:
    print(ex)
