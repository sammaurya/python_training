

# write another script to append counting of next 20 numbers. I.re 21 - 40

tableFile = open("/home/daffolap-876/PythonTraining/PythonAssignments/Assignment3/tableFile.txt", "a")
str = ""
for i in range(21, 41):
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