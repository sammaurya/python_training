
# Read the file created above and load it into dictionary in the format given below  
# My_dictionary =  {
# 2 : [2, 4, 6, 8, 10….]
# 3 : [3, 6, 9, 12...]
# }
# Note- Do not make dictionary using loop and multiplication. Make it using reading 
# the text from the file and then use string methods.


tableFile = open("/home/daffolap-876/PythonTraining/PythonAssignments/Assignment3/tableFile.txt", "r")
data = tableFile.readline()

myDict = {}

while data:
    list = data.split(":")
    key = int(list[0].strip())
    values = [ i.strip() for i in list[1].split(",")]

    myDict[key] = values
    data = tableFile.readline()

for key, values in myDict.items():
    print(key, values)