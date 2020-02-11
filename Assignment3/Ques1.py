
# write a python program to create a text file containing countings of 
# all the numbers from 1 to 20 in this  format :
#  	2 : 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# 3 : 3, 6, 9, 12, 15, 18, 21, 24, 27, 30… and so on.

with open("table_file.txt", "w") as table_file:
    str = ""
    for i in range(1, 21):

        str = str + "{} : ".format(i)
        for j in range(1, 11):
            if j == 10:
                str = str + "{}\n".format(i * j)
            else:
                str = str + "{}, ".format(i * j)

    table_file.write(str)