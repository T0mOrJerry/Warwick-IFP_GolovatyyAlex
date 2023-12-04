from math import pi


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def color(self):
        pass

    def __str__(self):
        return f'The shape has are {self.area()} and perimeter {self.perimeter()}, color - {self.color()}'


class Circle(Shape):
    def __init__(self, r, col):
        self.radius = r
        self.shape_color = col

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def color(self):
        return self.shape_color


class Rectangle(Shape):
    def __init__(self, lg, wd, col):
        self.length = lg
        self.width = wd
        self.shape_color = col

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

    def color(self):
        return self.shape_color


class Triangle(Shape):
    def __init__(self, a, b, c, col):
        self.a1 = a
        self.a2 = b
        self.a3 = c
        self.shape_color = col

    def perimeter(self):
        return self.a1 + self.a2 + self.a3

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a1) * (p - self.a2) * (p - self.a3)) ** 0.5

    def color(self):
        return self.shape_color


class Calculator:
    def add_shapes(self, *shapes):
        su = 0
        for i in shapes:
            su += i.area()
        return su


re = Rectangle(10, 8, 'green')
c = Circle(8, 'red')
tr = Triangle(3, 4, 5, 'black')
calc = Calculator()
print(calc.add_shapes(re, tr))
print(calc.add_shapes(re, tr, c))