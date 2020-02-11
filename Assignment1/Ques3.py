
# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = int(input("Enter odd number > 0 : "))

for i in range(1, n+1):
    if i <= (n+1)/2:
        stars = i+1
    else:
        stars = stars - 1
    for j in range(1, stars):
        print('*', end=' ')
    
    print()
