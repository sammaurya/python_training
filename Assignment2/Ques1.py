
# Ques1: 
# Given a list of tuples, the task is to remove all tuples having duplicate first values from the given list of tuples.
# Input:  [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]
# Output:  [('Tuple1', 121), ('Tuple2', 125), ('Tuple4', 478)]

input =  [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]

my_dict = {}
out_list = list(input)

for first, second in input:
    keys = my_dict.keys()
    if first in keys:
        to_remove = (first,second)
        out_list.remove(to_remove)
        continue
    else:
        my_dict[first] = second

print(out_list)