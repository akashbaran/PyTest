# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:04:23 2018

@author: eakabar

Question:

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

"""
s = input("enter the sentence ")
let, dig = 0,0
for i in s:
    if i.isalpha():
        let = let + 1
    elif i.isdigit():
        dig = dig + 1
    else:
        continue
print("LETTERS ",let)
print("DIGIT ",dig)
