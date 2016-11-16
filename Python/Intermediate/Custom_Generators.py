def simple_gen():
    yield "Oh"
    yield "Hello"
    yield "There"

for i in simple_gen():
    print(i)

correct_combo = (3, 6, 7, 9)
found = False

for c1 in range(10):
    if found:
        break
    for c2 in range(10):
        if found:
            break
        for c3 in range(10):
            if found:
                break
            for c4 in range(10):
                if (c1, c2, c3, c4) == correct_combo:
                    print("Found the combo: {}".format((c1, c2, c3, c4)))
                    found = True
                    break

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                for c4 in range(10):
                    yield (c1, c2, c3, c4)

for (c1, c2, c3, c4) in combo_gen():
    if (c1, c2, c3, c4) == correct_combo:
        print("Found the combo: {}".format((c1, c2, c3, c4)))
        break
