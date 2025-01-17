''' 
__________________________________________________________________
Author: Pranav Jain
Date: January 29, 2020
Student Number = 14213029
Source File: main.py

Course: MECH 550C - Software Design
Asignment Number: 2

Purpose: Compare area of two rectangles

Description:
This program compares area of two rectangles and prints True
if the area is equal and False if the area is different

Usage: Run main.exe
__________________________________________________________________
'''

def rectangleArea(l, w):
    """This is a function to calculate the area of a rectangle

    Arguments:
        l  -- length of the rectangle
        w  -- width of a rectangle

    Returns:
        a -- Area of the rectangle
    """
    a = l*w
    return a


length1 = 0.3
width1 = 3

length2 = 0.9
width2 = 1.0

rectArea1 = rectangleArea(length1, width1)
rectArea2 = rectangleArea(length2, width2)

x = (rectArea1 - rectArea2)<0.000001 or (rectArea1 - rectArea2)>0.000001 

print(x)

# input() command is used to exit the program when the users presses enter
input("\nPress Enter to Exit ")