# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:27:11 2018

@author: eakabar
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only.
"""
user = input("enter the username")
pat = "(\w+)@(\w+)\.(com)"
reg = re.match(pat, user)
print(reg.group(2))
