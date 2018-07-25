# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:48:51 2018

@author: eakabar

Write a program which accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

"""

s = input("enter 4 digit binary no sep by comma ")
seq = [seq for seq in s.split(",")]
res = []
i = 0
for i in seq:
    if int(i) % 5 == 0:
        res.append(i)
    else:
        continue
print(",".join(res))
