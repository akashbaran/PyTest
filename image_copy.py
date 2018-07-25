f1=open('book.jpeg','rb')
f2=open('book1.jpeg','wb')

bytes=f1.read()
f2.write(bytes)

f1.close()
f2.close()
