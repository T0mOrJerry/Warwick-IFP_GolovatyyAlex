class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rect1 = Rectangle(int(input('Input length: ')), int(input('Input width: ')))
print(f'The area is {rect1.area()}')