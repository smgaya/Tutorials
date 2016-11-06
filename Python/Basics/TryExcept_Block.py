import csv

with open("data.csv", "r") as f:
    data = csv.reader(f, delimiter=",")

    dates = []
    colours = []
    ages = []

    for d in data:
        colour = d[2]
        date = d[1]
        age = d[0]

        dates.append(date)
        colours.append(colour)
        ages.append(age)

    try:
        res = input("What colour do you want to know the data of? ")
        if res in colours:
            index = colours.index(res.lower())
            print("The date of ", colours[index], " is ", dates[index])
        else:
            print("Colour not in the list")
    except Exception as ex:
        print(ex)

    print("Try another colour")
