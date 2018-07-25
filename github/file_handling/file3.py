"""to print the file line wise, number of words, characters and lines"""

f = open("filename.txt","r+")
cl,cw,cc = 0,0,0
for line in f:
    word = line.split(" ")
    cw += len(word)
    cl += 1
    cc += len(line)

print("number of lines",cl)
print("number of words",cw)
print("number of characters",cc)

f.close()