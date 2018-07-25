"""Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10
"""
def EvenGen(n):
    i = 0
    while i<=n:
        if i%2 == 0:
            yield i
        i += 1

n = int(input("enter the value of n"))
values = []
for i in EvenGen(n):
    values.append(str(i))
print(','.join(values))