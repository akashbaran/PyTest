"""3. Write a Python program to append text to a file and display the text. """
txt = raw_input("enter text to append ")
fh = open("red.txt","a+")
if txt != 0:
    fh.write(txt + '\n')
fh.seek(0,0)
str = fh.read()
print(str)
fh.close()