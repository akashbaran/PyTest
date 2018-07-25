f=open('hello.txt','w')
#str = 'hello, how are u'
str=raw_input("enter text")
f.write(str)
f.close()
f1=open('hello.txt','r')
str1=f1.read()
print(str1)
f1.close()