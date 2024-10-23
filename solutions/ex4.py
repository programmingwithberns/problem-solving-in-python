""" 
You now own some property and you want to calculate the total area of the property.
Create a program that:
1. Reads the width and height
2. Prints the area
Example: width = 5, height = 2
Output: total_area = 10
"""
from utils import get_float 

width = get_float("Please enter the width: ", 1, 1000)

length = get_float("Please enter the length: ", 1, 1000) 

area = length * width 


print(f"The area of the property with width {width} m and length {length} m is {area} sq.m")