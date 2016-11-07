xyz = [i for i in range(5)]
print(xyz)

xyz = (i for i in range(5))
print(xyz)

for i in xyz:
    print(i)
    