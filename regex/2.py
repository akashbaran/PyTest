"""Write a Python program that matches a string that has an a followed by zero or more b's"""

import re

str = raw_input("enter the string ")
prog = re.compile(r'a[0b*]')
res = prog.search(str)

if res:
    print("found",res.group())
else:
    print("nt found")