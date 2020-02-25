
'''
Create a stack class with push and pop operations
Also create two custom exceptions one for Underflow condition and one for Overflow 
condition that will be raised when stack underflow or overflow condition occurs
'''

class UnderflowError(Exception):
    def __init__(self, e):
        self.e = e
    
    def __str__(self):
        return e

class OverflowError(Exception):
    def __init__(self, e):
        self.e = e
    
    def __str__(self):
        return str(self.e)

class Stack:

    def __init__(self, size):
        self._list = []
        self._size = size

    def push(self, value):
        if len(self._list) < self._size:
            self._list.append(value)
        else:
            raise OverflowError("OverflowError : Stack is full")

    def pop(self):
        if len(self._list) > 0:
            return self._list.pop()
        else:
            raise UnderflowError("UnderflowError : Stack is empty")

    def __str__(self):
        return "".join(str(value) + ", " for value in self._list)

stack = Stack(4)

try:
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(7)
    print(stack)
    stack.pop()
    stack.push(8)
    print(stack)
    stack.push(10)
except OverflowError as e:
    print(e)
except UnderflowError as e:
    print(e)
except:
    print("Error occurred")


