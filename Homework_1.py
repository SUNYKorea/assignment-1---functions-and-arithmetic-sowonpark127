# Name:Sowon Park  
# SBUID: 115242731
##################### SCORE ######################
####### good work Score:  8/10
#################################################
# Remove the ellipses (...) when writing your solutions.
# your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/sowonpark127/Homework_1.py"
# Please enter a temperature in degree Fahrenheit: 44
# Sweater --> correct
# x1: -4
# y1: -4
# x2: -5
# y2: 5
# x3: 3
# y3: -3
# The area of the triangle is : 32.0 , its perimeter is : 27.440161448987652--> correct
# The area of the polygon is : 236.59292911256335 --> wrong
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
    celsius = (5/9)*(fahrenheit - 32)
    return celsius   

def what_to_wear(celsius):
    if celsius < -10:
        print("Puffy jacket")
    elif celsius <= 0:
        print("Scarf")
    elif celsius <= 10:
        print("Sweater")
    elif celsius <= 20:
        print("Light jacket")
    else:
        print("T-shirt")
        
fahrenheit = int(input("Please enter a temperature in degree Fahrenheit: "))
what_to_wear(fahrenheit2celsius(fahrenheit))

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  


def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    A1 = abs((x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)/2)
    return A1

def euclidean_distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x3, y3, x1, y1)
    s = s1 + s2 + s3
    return s

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
x3 = int(input('x3: '))
y3 = int(input('y3: '))
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    import math
    r = deg*math.pi/180
    return r

def apothem(number_sides, length_side):
    import math
    a = length_side/(2*math.tan(deg2rad((180/number_sides))))
    return a

def polygon_area(number_sides, length_side):
    a = apothem(number_sides, length_side)
    A2 = number_sides*length_side*a/2
    return A2


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
#fahrenheit = 40
#what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
# x1, x2, x3, y1, y2, y3 = 1,3,5,2,4,6 # declaration of the vertices of the triangle
# area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
# perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
# print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# # Exercise 3 test
number_sides = 8
length_side = 7
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

