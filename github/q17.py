# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:32:45 2018

@author: eakabar

Question:
Write a program that computes the net amount of a bank account based a transaction log
 from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

"""
net = 0
while True:
    s = input("input transaction logs ")
    if not s:
        break
    val = s.split(" ")
    op = val[0]
    am = int(val[1])
    if op == "D":
        net = net + am
    elif op == "W":
        net = net - am
    else:
        pass
print(net)

