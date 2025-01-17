import math


def calculate_circle_area(radius):
    return math.pi * radius ** 2


while True:
    radius = input("Enter the radius of your circle: ")

    try:
        radius_value = float(radius)
        area = calculate_circle_area(radius_value)
        print(f'The area of your circle is {area:.2f}')
        break
    except ValueError:
        print(f'Your value "{radius}" isn`t a valid number, please try again!')
