import timeit

print(timeit.timeit("""input_list = range(100)

def div_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False

# Generator
gen = (i for i in input_list if div_by_five(i)) """, number=10000))

print(timeit.timeit("""input_list = range(100)

def div_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False

# List
gen = [i for i in input_list if div_by_five(i)] """, number=10000))