
'''
Create a stack class with push and pop operations
Also create two custom exceptions one for Underflow condition and one for Overflow 
condition that will be raised when stack underflow or overflow condition occurs
'''

class Error(Exception):
    pass

class UnderflowError(Error):
    pass

class OverflowError(Error):
    pass

class Stack:

    def __init__(self, size):
        self._list = []
        self._size = size

    def push(self, value):
        try:
            if len(self._list) < self._size:
                self._list.append(value)
            else:
                raise OverflowError
        except OverflowError:
            print("OverflowError: Stack is full")

    def pop(self):
        try:
            if len(self._list) > 0:
                return self._list.pop()
            else:
                raise UnderflowError
        except UnderflowError:
            print("UnderflowError : Stack is empty")

    def __str__(self):
        return "".join(str(value) + ", " for value in self._list)

s = Stack(4)
s.pop()
s.push(2)
s.push(4)
s.push(6)
s.push(7)
print(s)
s.pop()
s.push(8)
print(s)
s.push(10)


