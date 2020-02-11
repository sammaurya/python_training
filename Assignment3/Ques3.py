
# Read the file created above and load it into dictionary in the format given below  
# My_dictionary =  {
# 2 : [2, 4, 6, 8, 10….]
# 3 : [3, 6, 9, 12...]
# }
# Note- Do not make dictionary using loop and multiplication. Make it using reading 
# the text from the file and then use string methods.


with open("table_file.txt", "r") as table_file:

    my_dict = {}

    for data in table_file:
        list = data.split(":")
        key = int(list[0].strip())
        values = [ i.strip() for i in list[1].split(",")]
        my_dict[key] = values

    for key, values in my_dict.items():
        print(key, values)