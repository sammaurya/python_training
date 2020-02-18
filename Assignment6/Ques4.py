'''
We have a function named calculate_sum(list) which is calculating the sum of the list. 
Someone wants to modify the behaviour in a way such that:
1. It should calculate only sum of even numbers from the given list.
2. Obtained sum should always be odd. If the sum is even, make it odd by adding +1 and
    if the sum is odd do nothing
Write two decorators that would serve these two purposes and use them in the above function.
'''

def even_sum(func):
    def wrapper(list):
        even_list = [value for value in list if value % 2 == 0]
        return func(even_list)

    return wrapper

def make_odd(func):
    def wrapper(list):
        sum = func(list)
        if sum % 2 == 0:
            return sum + 1
        return sum
    return wrapper 

@make_odd
@even_sum
def calculate_sum(list):
    return sum(list)

list = [1,2,3,4,5,6,7,8,9,10]
print(calculate_sum(list))