
'''
Create a stack class with push and pop operations
Also create two custom exceptions one for Underflow condition and one for Overflow 
condition that will be raised when stack underflow or overflow condition occurs
'''

class Stack:

    def __init__(self, size):
        self.list = []
        self.size = size

    def push(self, value):
        if len(self.list) < self.size:
            self.list.append(value)
        