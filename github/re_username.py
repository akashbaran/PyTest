# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:06:58 2018

@author: eakabar

Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.

"""

"""
Without using regular expression:
    
s = input("enter the email id ")
lst = []
lst = s.split("@")
print("username is ",lst[0])
"""
from re import split
user = input("enter the username ")
lst = split('\W+',user)
print(lst[0])

