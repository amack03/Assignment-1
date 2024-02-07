'''
This program will,

    1. Calculate the circumference of a circle.
    2. Calculate the area of a circle.
'''

import math

radius = int(input("Enter the radius of a circle: "))
circumference = 2 * (math.pi * radius)
area = math.pi * (radius ** 2)

print(f"The circumference of the circle is {circumference}")
print(f"The area of the circle is {area}")