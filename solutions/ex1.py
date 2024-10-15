"""
Create two variables a and b, and initially set them each to a different number.
Write a program that swaps both values.

* Example: a = 10, b = 20
* Output: a = 20, b = 10
"""

a = 10
b = 20 
print(f"Step0: a={a}, b={b}")

tmp = a 

print(f"Step1: a={a}, b={b}, tmp={tmp}")
a = b
print(f"Step2: a={a}, b={b}, tmp={tmp}")

b = tmp 
print(f"Results: a={a}, b={b}, tmp={tmp}")

# one liner 
# a, b = b, a 
