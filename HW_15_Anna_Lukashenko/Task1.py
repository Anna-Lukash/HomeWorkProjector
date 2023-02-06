''' 1) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.'''
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    #method which will compute the area of circle
    def area(self):
        return round((self.radius ** 2) * math.pi, 4)
    #method which will compute the perimeter of circle
    def perimeter(self):
        return round(2 * self.radius * math.pi, 4)
    
circle1 = Circle(14)
print(circle1.area()) 
print(circle1.perimeter())
