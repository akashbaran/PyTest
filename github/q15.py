# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:16:37 2018

@author: eakabar
Question
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

n = int(input("enter the no "))
#n1 = int("%s",)
n1 = int( "%s" % n )
n2 = int( "%s%s" % (n,n) )
n3 = int( "%s%s%s" % (n,n,n) )
n4 = int( "%s%s%s%s" % (n,n,n,n) )
res = n1 + n2 + n3 + n4
print(res)

