"""Write a Python program to count the number of lines in a text file."""

def count_lines(filename):
    with open(filename,"r") as fh:
        files = fh.read().split('\n')
    return len(files)
print(count_lines("red.txt"))