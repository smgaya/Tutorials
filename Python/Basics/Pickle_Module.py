import pickle

dict = {1: "a", 2: "c", 3: "f"}

pickle_out = open("dict.pickle", "wb")
pickle.dump(dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle", "rb")
dict = pickle.load(pickle_in)

print(dict)
print(dict[3])
