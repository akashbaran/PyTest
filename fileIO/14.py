"""14. Write a Python program to combine each line from first file with the corresponding line in second file."""

fname1 = open("red.txt","r")
fname2 = open("destination.txt","r")

str1 = fname1.read().split('\n')
str2 = fname2.read().split('\n')

l1,l2 = len(str1),len(str2)
if l1 > l2:
    l = l2
else:
    l = l1

for i in range(l):
    print(str1[i] + '\t' + str2[i])
