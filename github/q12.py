# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:56:17 2018

@author: eakabar

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""

res = []
n = 1000

for n in range(1000,3001):
    s = str(n)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        res.append(s)
print(",".join(res))
