"""
enter a sequence of strings and print the count of each character
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

str2 = raw_input("enter the sequence ")
print(char_frequency(str2))