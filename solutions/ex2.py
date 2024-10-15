"""
It's the end of the semester and you got your grades from three 
classes: Geometry, Algebra, and Physics.

Create a program that:
1) Reads the grades of these 3 classes (Grades range from 0 - 10)
2) Calculate the average of your grades

* Example: Geometry = 6, Algebra = 7, Physics = 8
* Output: average_score = 7 
"""

# input 
geometry = float(input("Please enter your grades for Geometry: "))

algebra = float(input("Please enter your grades for Algebra: "))

physics = float(input("Please enter your grades for Physics: "))

# processing 
if geometry < 0 or geometry > 10 or algebra < 0 or algebra > 10 or physics < 0 or physics > 10:
    print(f"Invalid values entered for grades. Grades range from 0 - 10")
else: 
    sum_of_grades = geometry + algebra + physics
    print(f"Sum of grades [geo={geometry}, alg={algebra}, phy={physics}] is {sum_of_grades}")

    average = sum_of_grades / 3 
    print(f"Average of grades [geo={geometry}, alg={algebra}, phy={physics}] is {average}")