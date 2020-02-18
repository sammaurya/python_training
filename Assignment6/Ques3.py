'''
We have a bookshop, in which orders are stored in format like this: 
[
[order_number 1, (book number 1, quantity, price per unit), ... 
(book number 10, quantity, price per unit), [order_number 2, ……………...]] 
Write a program which returns a list of two tuples with (order number, total amount of order).
From this returns a list of order numbers for which total amount > x
Sample data:
[ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
In 2nd point consider x to be 400
'''

from functools import reduce

bookshop = [ 
            [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	        [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	        [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
            [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)], 
            [5, ("7732", 5, 15.99), ("7823",4,28.99), ("98212", 2, 59.95)] 
        ]
'''
With the use of normal for loop and if-else
'''
# order_list = []
# for order in bookshop:
#     order_no = order[0]
#     total_amt = 0
#     for book_no, qty, price in order[1:]:
#         total_amt += qty * price 
#     order_list.append((order_no, round(total_amt, 2)))

# print(order_list)
# x = int(input("Enter the value of x : "))
'''
This will give the original list having 
total_amount > x
'''
# order_x = []
# for order_no, total_amt in order_list:
#     if total_amt > x:
#         for order in bookshop:s
#             if order[0] == order_no:
#                 order_x.append(order)
#                 break
'''
This will give order numbers having
total_amount > x
'''
# order_x = []
# for order_no, total_amt in order_list:
#     if total_amt > x:
#         order_x.append(order_no)
# print(order_x)

'''
With the use of list comprehension and reduce function
'''
order_list = [(order[0], round(sum([qty * price for _, qty, price in order[1:] ]), 2)) for order in bookshop ]

print(order_list)

x = int(input("Enter the value of x : "))
'''
This will give the original list having 
total_amount > x
'''
# order_x = [order for order_no, total_amt in order_list if total_amt > x for order in bookshop  if order_no == order[0]]

# print(order_x)
'''
This will give order numbers having
total_amount > x
'''
order_x = [order_no for order_no, total_amt in order_list if total_amt > x]
print(order_x)