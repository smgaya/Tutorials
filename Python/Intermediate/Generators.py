input = [4, 3, 12, 5, 65, 76, 88, 90, 0, 46]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input if div_by_five(i))
[print(j) for j in xyz]

[print(i, ii) for ii in range(1, 5) for i in range(1, 5)]
