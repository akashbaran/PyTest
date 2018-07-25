"""1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)"""

import re

str = raw_input("enter the string ")

prog = re.compile(r'^[a-zA-Z0-9]$')
res = prog.search(str)
if res:
    print("contains the set")
else:
    print("not found")
#print(res.group())