"""Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string."""

import re

str = raw_input("enter the string ")
prog = re.compile(r'[0-9]')
res = prog.search(str)

if res:
    print("found", res.group())
else:
    print("nt found")