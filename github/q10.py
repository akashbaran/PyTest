# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:39:03 2018

@author: eakabar

Question:
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them 
alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

"""


inp = input("enter the sequence ")
words = [ words for words in inp.split(" ")]
print(" ".join(sorted(list(set(words)))))