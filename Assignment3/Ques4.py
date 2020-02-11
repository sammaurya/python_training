
# Once done with creating the dictionary file then dump the dictionary object using pickle.

import pickle



tableFile = open("/home/daffolap-876/PythonTraining/PythonAssignments/Assignment3/tableFile.txt", "r")
data = tableFile.readline()

myDict = {}

while data:
    list = data.split(":")
    key = int(list[0].strip())
    values = [ i.strip() for i in list[1].split(",")]

    myDict[key] = values
    data = tableFile.readline()

pickleFile = open("/home/daffolap-876/PythonTraining/PythonAssignments/Assignment3/tableDict.pickle", "wb")
pickle.dump(myDict, pickleFile)
pickleFile.close()

