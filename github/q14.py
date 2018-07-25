# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:10:15 2018

@author: eakabar

Write a program that accepts a sentence and calculate the number of upper case
letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
sent = input("enter the sentence ")
LOWER,UPPER=0,0
for i in sent:
    if i.islower():
        LOWER = LOWER + 1
    elif i.isupper():
        UPPER = UPPER + 1
    else:
        continue
print("UPPER CASE ",UPPER)
print("LOWER CASE ",LOWER)        
