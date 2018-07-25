import os, sys
fname=raw_input("enter file name\n")


if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname + " does not exist")
    sys.exit()

cl=cw=cc=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)

print('no of line',cl)
print('no of words',cw)
print('no of chars',cc)

f.close()