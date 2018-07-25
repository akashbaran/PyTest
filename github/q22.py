# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:53:35 2018

@author: eakabar
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
#will be using disctionary for this
freq = {}
line = input()
for word in line.split():
#get returns the value for that word, in case no value is returned 
#second argument is taken as default value
    freq[word] = freq.get(word,0) + 1
words = list(freq.keys())
words.sort()

for w in words:
    print("%s:%d" %(w, freq[w]))
    

