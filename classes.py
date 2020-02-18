
# class A:
#      def __init__(self):
#          self.name = "sam"
#          self._num = 9 #protected
#          self.__age = 22 #private

# a = A()
# print(a.name, a._num)
# a.__age = 23
# print(a._A__age)   
# print(dir(a))

# a = 8
# b=10
# print(a.__add__(2))

# for i in range(5):
#     print(i)
# print(range(5))

# class Parent:
#     def __init__(self,name='Parent',age='52'):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return "{0.name} is {0.age} years old.".format(self)
    
# class Child(Parent):
#     def __init__(self, name='child',parent='Parent',age='52'):
#         super().__init__(parent,age)
#         self.name = name

#     def do(self):
#         print("Doing...")

#     def __str__(self):
#         return "Hey Child"


# c = Child('sam','rahul','22')
# c.do()
# p = Parent('Rakesh','45')
# print(p)
# # p.do()
# print(c)

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.i, MyClass.f(MyClass))
print(MyClass().f())
print(type(MyClass.f))