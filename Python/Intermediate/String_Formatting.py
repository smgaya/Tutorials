import os

names = ["Jeff", "Gary", "Jill", "Samantha"]

# for name in names:
#     print("Hello there, " + name)
#     print(" ".join(["Hello there,", name]))

# print(", ".join(names))

file_dir = "C:\\Software_Development\\Tutorials\\Python\\Intermediate\\"
file_name = "String_Formatting.py"

# print(file_dir + "\\" + file_name)

# with open(os.path.join(file_dir, file_name)) as f:
#     print(f.read())

who = "Gary"
how_many = 12

print(who, "bought", how_many, "apples today!")
print("{} bought {} apples today!".format(who, how_many))
