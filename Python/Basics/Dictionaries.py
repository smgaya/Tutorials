x = {"Jack": [15, "blonde"], "Bob": [22, "brown"], "Alice": [12, "black"], "Kevin": [17, "ginger"]}

print(x)
print(x["Jack"])

x["Tim"] = 14
print(x)

x["Tim"] = 15
print(x)

del x["Tim"]
print(x)

print(x["Jack"][1])
