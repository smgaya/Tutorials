x = [1, 2, 3, 4, 5]
y = [5, 6, 3, 2, 8]
z = ["a", "b", "c", "d", "e"]

for a, b, c in zip(x, y, z):
    print(a, b, c)

print(zip(x, y, z))

for i in zip(x, y, z):
    print(i)
    