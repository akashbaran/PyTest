"""2. Write a Python program to read first n lines of a file."""

lines = raw_input("enter the number of lines to read  ")
line = int(lines)
fh = open("red.txt","r")
str = fh.read().split("\n")
for i in range(line):
    print(str[i])

#print(str)


#from itertools import islice

