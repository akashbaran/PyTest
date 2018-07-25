"""15. Write a Python program to read a random line from a file. """

import random
fname = open("red.txt","r")
lines = fname.read().split('\n')
print(random.choice(lines))