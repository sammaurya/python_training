
# Once done with creating the dictionary file then dump the dictionary object using pickle.

import pickle



with open("table_file.txt", "r") as table_file:


    my_dict = {}

    for data in table_file:
        list = data.split(":")
        key = int(list[0].strip())
        values = [ i.strip() for i in list[1].split(",")]
        my_dict[key] = values

with open("table_dict.pickle", "wb") as pickle_file:
    pickle.dump(my_dict, pickle_file)


