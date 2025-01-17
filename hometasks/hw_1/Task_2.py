import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def __str__(self):
        return (f'It`s your area: {self.area()}\n'
                f'It`s your perimeter: {self.perimeter()}\n'
                f'Your Rectangle is square? {self.is_square()}\n'
                f'See you later :*\n\n')


r1 = Rectangle(2, 4)
print(r1)

r1.resize(5, 5)
print(r1)
