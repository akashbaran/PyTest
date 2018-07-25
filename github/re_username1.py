# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:25:27 2018

@author: eakabar
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.
"""

import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))