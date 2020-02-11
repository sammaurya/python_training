
# Write a python program to load the dictionary created above 
# and then take user input and then print table list on console.

import pickle

with open("table_dict.pickle", "rb") as pickle_file:
    my_dict = pickle.load(pickle_file)
    key = int(input("Enter a number [1-40] : "))

    if key > 0 and key < 41:
        print(my_dict[key])
    else:
        print("Out of Range")