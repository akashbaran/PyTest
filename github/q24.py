# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:37:16 2018

@author: eakabar

 Python has many built-in functions, and if you do not know how to use it,
 you can read document online or find some books. 
 But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents,
such as abs(), int(), raw_input()
    And add document for your own function
"""

#for abs() 
print(abs.__doc__)
#for input function
print(input.__doc__)

def square(num):
    """this func returns the square of the input number"""
    return(num**2)

print("Square of number 4 is ",square(4))
print(square.__doc__)
