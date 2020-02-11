
# write a python program to create a text file containing countings of 
# all the numbers from 1 to 20 in this  format :
#  	2 : 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# 3 : 3, 6, 9, 12, 15, 18, 21, 24, 27, 30… and so on.

tableFile = open("/home/daffolap-876/PythonTraining/PythonAssignments/Assignment3/tableFile.txt", "w")
str = ""
for i in range(1, 21):
    # print(i, end=" : ")
    str = str + "{0:2} : ".format(i)
    pos = 1
    for j in range(i, i*10+1,i*pos):
        if j == i*10:
            str = str + "{0:3}\n".format(j)
        else:
            str = str + "{0:3}, ".format(j)

        pos = pos + 1
    
# print(str)

tableFile.write(str)
tableFile.close()