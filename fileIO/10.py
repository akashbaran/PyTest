"""10. Write a Python program to count the frequency of words in a file."""
"""
def frequency(filename):
    with open(filename, "r") as fh:
        words = fh.read().split()
    l = len(words)
    new_dict = {}
    for i in words:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1

    return new_dict

print(frequency("red.txt"))"""

from collections import Counter
def freq(filename):
    with open(filename,"r") as fh:
        words = fh.read().split()
    c = Counter(words)
    return c

print(freq("red.txt"))