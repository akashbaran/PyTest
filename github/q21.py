# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:34:34 2018

@author: eakabar
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. 
Please write a program to compute the distance from current position 
after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5 
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
import math
l,r=0,0
while True:
    s = input("enter direction ")
    if not s:
        break
    lst = s.split(" ")
    dir=lst[0]
    pos=int(lst[1])
    if dir == 'UP':
        r = r + pos
    elif dir == 'DOWN':
        r = r - pos
    elif dir == 'LEFT':
        l = l - pos
    elif dir == 'RIGHT':
        l = l + pos
    else:
        pass
res = int(math.sqrt((l**2) + (r**2)))
print(res)  
    