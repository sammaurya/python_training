
# Ques1: 
# Given a list of tuples, the task is to remove all tuples having duplicate first values from the given list of tuples.
# Input:  [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]
# Output:  [('Tuple1', 121), ('Tuple2', 125), ('Tuple4', 478)]

input =  [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]

myDict = {}

for first, second in input:
    keys = myDict.keys()

    if first in keys:
        toRemove = (first,second)
        input.remove(toRemove)
        continue
    else:
        myDict[first] = second

print(input)