# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:31:22 2018

@author: eakabar
Write a program which accepts a sequence of words separated by whitespace
as input to print the words composed of digits only.

"""
import re
inp = input("enter the sequence")
res = re.findall('\d',inp)
print(res)
