
# Print all palindrome numbers from 10 to 999999 using generators.

# def palindrome(start, end):    
#     for num in range(start, end):
#         num = str(num)
#         length = len(num)
#         if length % 2 != 0:
#             mid = length // 2
#             if num[mid-1::-1] == num[mid+1:]:
#                 yield num
#         else:
#             mid = (length // 2) - 1
#             if num[mid::-1] == num[mid+1:]:
#                 yield int(num)
        
        
def palindrome(start, end):
    for num in range(start, end):
        num = str(num)
        if num == num[::-1]:
            yield int(num)

for num in palindrome(10,100):
    print(num, end=", ")

