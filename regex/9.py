"""Write a Python program to check for a number at the end of a string."""


import re

ip = raw_input("enter the string")
prog = re.compile(r'[0-9]$')
res = prog.search(ip)
if res:
    print("found", res.group())
else:
    print("nt found")