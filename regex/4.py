"""Write a Python program that matches a string that has an a followed by two to three 'b'"""

import re

str = raw_input("enter the string ")
prog = re.compile(r'ab{2,3}')
res = prog.search(str)

if res:
    print("found",res.group())
else:
    print("nt found")