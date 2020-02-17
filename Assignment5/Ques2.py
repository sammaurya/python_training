"""
1. Create a super class called Car. The Car class has the following properties. 
    Speed; regularPrice; color;
    It should have a method doublegetSalePrice() which will return the sale price of the car.
2. Create a sub class of Car class and name it as Truck. The Truck class has a field : weight.
    Override doublegetSalePrice() in a way that If weight>2000 then 10% discount, Otherwise no discount
3. Create a subclass of Car class and name it as Ford. The Ford class has a field manufacturer Discount.
    Override doublegetSalePrice() in a way that it will always subtract the manufacturer Discount.

4. Create a subclass of Car class and name it as Sedan. The Sedan class has a field length. Override 
    doublegetSalePrice() in a way that If length > 20 feet, 5% discount, Otherwise , 10% discount.

Create instances of all type of cars and show the sale price of all of them.
"""

class Car:
    
    def __init__(self, speed, regularPrice, color):
        self.speed = speed
        self.regularPrice = regularPrice
        self.color = color

    def doublegetSalePrice(self):
        return self.regularPrice

    
class Truck(Car):

    def __init__(self,weight, speed, regularPrice, color):
        super().__init__(speed, regularPrice, color)
        self.weight = weight

    def doublegetSalePrice(self):
        if self.weight > 2000:
            return self.regularPrice * 0.9
        else:
            return self.regularPrice 

class Ford(Car):

    def __init__(self, manufacturerDiscount, speed, regularPrice, color):
        super().__init__(speed, regularPrice, color)
        self.manufacturerDiscount = manufacturerDiscount
    
    def doublegetSalePrice(self):
        return self.regularPrice * (100 - self.manufacturerDiscount)/100

class Sedan(Car):

    def __init__(self, length, speed, regularPrice, color):
        super().__init__(speed, regularPrice, color)
        self.length = length

    def doublegetSalePrice(self):
        if self.length > 20:
            return self.regularPrice * 0.95
        else:
            return self.regularPrice * 0.90            


truck = Truck(2100, 50, 60,'white')
print(truck.doublegetSalePrice())

ford = Ford(10, 150, 150, 'blue')
print(ford.doublegetSalePrice())

sedan = Sedan(20, 120, 12, 'maroon')
print(sedan.doublegetSalePrice())
