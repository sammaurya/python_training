"""
Write an base class name Shape that have a abstract method: def area()
ALso have a class method name get() which accepts a name of the shape 
and returns the child class object

Child classes will implement how to compute the area. Take at least 
three child classes and show computed area for each shape
"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @classmethod        
    def get(cls, name):
        if name == 'Circle':
            return Circle()
        elif name == 'Triangle':
            return Triangle()
        elif name == 'Square':
            return Square()

class Circle(Shape):

    def __init__(self):
        self._radius = 0

    def area(self):
        return pi * self._radius**2

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        
class Triangle(Shape):
    
    def __init__(self):
        self._length = 0
        self._breadth = 0

    def area(self):
        return 0.5 * self._length * self._breadth
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        self._length = length

    @property
    def breadth(self):
        return self._breadth
    
    @breadth.setter
    def breadth(self, breadth):
        self._breadth = breadth

class Square(Shape):
    
    def __init__(self):
        self._side = 0


    def area(self):
        return self._side * self._side
    
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, side):
        self._side = side


circle = Shape.get('Circle')
circle.radius = 2
print("Area of Circle with radius {0} is {1}".format(circle.radius, circle.area()))

triangle = Shape.get('Triangle')
triangle.length = 2
triangle.breadth = 3
print("Area of triangle with l = {0}, b = {1} is {2}".format(triangle.length, 
                                            triangle.breadth, triangle.area()))
square = Shape.get('Square')
square.side = 4
print("Area of square with side {0} is {1}".format(square.side, square.area()))
