"""16. Write a Python program to assess if a file is closed or not."""

#fn = raw_input("enter the filename")
fname = open("red.txt","r")
print(fname.closed)
fname.close()
print(fname.closed)
