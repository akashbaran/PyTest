"""12. Write a Python program to write a list to a file."""


lst = [1, 2, 3, 4, 5, 6]
with open("red1.txt","a+") as myfile:
    myfile.write(str(lst))
myfile.close()
content = open("red1.txt")
print(content.read())