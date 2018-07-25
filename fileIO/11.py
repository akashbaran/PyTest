"""1. Write a Python program to get the file size of a plain file. """

import os
def file_size(filename):
    size = os.stat(filename)
    return size
print(file_size("red.txt"))