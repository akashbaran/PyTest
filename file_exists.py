import os, sys
fname=raw_input("enter filename: ")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname + " does not exist\n")
    sys.exit()

print('the file contents are:\n')
str=f.read()
print(str)