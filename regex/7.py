"""Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'"""

import re
str = raw_input("enter the string")
prog = re.compile(r'a[A-Z]*[a-z]*[0-9]*b')
res = prog.search(str)

if res:
    print("found", res.group())
else:
    print("nt found")