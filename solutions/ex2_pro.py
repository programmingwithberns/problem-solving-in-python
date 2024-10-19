"""
It's the end of the semester and you got your grades from three 
classes: Geometry, Algebra, and Physics.

Create a program that:
1) Reads the grades of these 3 classes (Grades range from 0 - 10)
2) Calculate the average of your grades

* Example: Geometry = 6, Algebra = 7, Physics = 8
* Output: average_score = 7 
"""

from utils import get_float
# input 
geometry = get_float("Please enter your grades for Geometry: ", 0, 10)

algebra = get_float("Please enter your grades for Algebra: ", 0, 10)

physics = get_float("Please enter your grades for Physics: ", 0, 10)

# processing 
sum_of_grades = geometry + algebra + physics

average = sum_of_grades / 3 

# output
print(f"Sum of grades [geo={geometry}, alg={algebra}, phy={physics}] is {sum_of_grades}")

print(f"Average of grades [geo={geometry}, alg={algebra}, phy={physics}] is {average}")