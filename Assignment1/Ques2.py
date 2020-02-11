

# We have a string s, s = '12345' * 5. 
# Produce following ouput by using string slicing:
# 1. '11111'
# 2. '55555'
# 3. Reverse the string


s = '12345' * 5

print(s[: len(s)-4: 5])
print(s[4: len(s): 5])
print(s[::-1])