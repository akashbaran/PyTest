# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:26:55 2018

@author: eakabar

Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

"""
res = []
s = input("enter sep by comma")
lst = [lst for lst in s.split(',')]
for i in lst:
    if int(i)%2 != 0:
        sq = int(i)**2
        res.append(str(sq))
print(",".join(res))