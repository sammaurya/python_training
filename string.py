# print('Hello' + ' ' + 'World!')

# only str concate not int with str 
# print('Helllo' + ' ' + 23)

# print(type('sam'))
# print(type(123))
# print(type(123.45))
# print(type(True))
# print(type([]))
# print(type({}))
# print(type(()))


# s = '12345'
# print(s*5)

# for i in range(18):
#     print("{0:>2} in binary is {0:08b}".format(i))

# million = 1_000_000
# binary = 0b_0010
# octa = 0o_64
# hexa = 0x_23_ab

# print(million)
# print(binary)
# print(octa)
# print(hexa)

class A:
     def __init__(self):
         self.name = "sam"
         self._num = 9

a = A()
print(a.name, a._num)