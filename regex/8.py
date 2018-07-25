"""Write a Python program to remove leading zeros from an IP address. """

import re

ip = raw_input("enter the ip address")
#02.433.1233.43
res = []
prog = re.compile(r'[.]')
lst1 = prog.split(ip)
for i in lst1:
    res.append(str(int(i)))

print(".".join(res))

