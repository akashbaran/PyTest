"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""
class testStr:
    def __init__(self):
        self.s = ""
    def getStr(self):
        self.s = raw_input()
    def printStr(self):
        print(self.s.upper())

obj = testStr()
obj.getStr()
obj.printStr()
