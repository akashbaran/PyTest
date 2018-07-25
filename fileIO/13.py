"""13. Write a Python program to copy the contents of a file to another file ."""

with open("red.txt", "r") as fname:
    words = fname.read()

for line in words:
    fh = open("destination.txt","a+")
    fh.write(line)

fh.seek(0,0)
str = fh.read()
print(str)