# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:51:53 2018

@author: eakabar
Write a function to compute 5/0 and use try/except to catch the exceptions.

"""
def throw():
    return(5/0)

try:
    throw()
except ZeroDivisionError:
    print("divided by zero!/0")
except Exception:
    print("caught an exception")
finally:
    print("print final block")

