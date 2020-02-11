

# write another script to append counting of next 20 numbers. I.re 21 - 40

with open("table_file.txt", "a") as table_file:
    str = ""
    for i in range(21, 41):
        
        str = str + "{} : ".format(i)
        for j in range(1, 11):
            if j == 10:
                str = str + "{}\n".format(i * j)
            else:
                str = str + "{}, ".format(i * j)

    table_file.write(str)
