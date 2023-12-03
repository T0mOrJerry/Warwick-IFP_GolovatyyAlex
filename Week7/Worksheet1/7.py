from math import pi


class Circle:
    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    
circ1 = Circle(int(input('Input radius: ')))
print(f'The area is {circ1.area()}')
print(f'The perimeter is {circ1.perimeter()}')