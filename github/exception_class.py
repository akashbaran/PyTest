# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:56:00 2018

@author: eakabar
Define a custom exception class which takes a string message as attribute.
"""

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
print(error)