"""Write a Python program to find sequences of one upper case letter followed by lower case letters."""

import re
str = raw_input("enter the string")
prog = re.compile(r'[A-Z][a-z]+')
res = prog.search(str)

if res:
    print("found", res.group())
else:
    print("nt found")