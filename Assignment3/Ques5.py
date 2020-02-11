
# Write a python program to load the dictionary created above 
# and then take user input and then print table list on console.

import pickle

pickleFile = open("/home/daffolap-876/PythonTraining/PythonAssignments/Assignment3/tableDict.pickle", "rb")
myDict = pickle.load(pickleFile)

key = int(input("Enter a number [1-40] : "))

if key > 0 and key < 41:
    if key in myDict.keys():
        print(myDict[key])
else:
    print("Out of Range")