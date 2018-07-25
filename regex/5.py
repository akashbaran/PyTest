"""Write a Python program to find sequences of lowercase letters joined with a underscore"""

import re
str = raw_input("enter the string")
prog = re.compile(r'_[a-z]*_')
res = prog.search(str)

if res:
    print("found", res.group())
else:
    print("nt found")