
# if-elif-else 
# x = int(input("Enter an Integer : "))

# if x < 0:
#     x = 0
#     print('Negative changed to Zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:    
#     print('More')

# for-in

# words = ['cat', 'window', 'porsche']

# for w in words:
#     print(w, len(w))


# for-in-range(n) n is not inclusive

# for i in range(5):
#     print(i)

# a = ['Rahul', 'is', 'a', 'site', 'engineer']

# for i in range(len(a)):
#     print(i, a[i])

# print(sum(range(10)))

# a = list(range(4))
# print(a)

# for x in range(2,3):
#     print(x)

# Prime Number to 10
# here else belongs to the for loop not the if
# else runs when there is an exception or break occurs
# it is behaving like a try-catch block

# for n in range(2, 11):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#             print(n, 'is a prime number')


# Fibonacci series upto n

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     # print()

# # fib(100)
#  function by default return None
# print(fib(1))

# def fib(n):
#     '''Return  a list of fibonacci series to n'''
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
    
#     return result

# f10 = fib(10)
# print(f10)

