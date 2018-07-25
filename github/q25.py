# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:42:36 2018

@author: eakabar

Question:
    Define a class, which have a class parameter and have a same instance parameter.

"""
class Person:
    name = "Person"
    
    def __init__(self, name = None):
        self.name = name
jef = Person("Jeff")
print("%s name is %s" % (Person.name, jef.name))

nico = Person()
nico.name = "Akash"
print("%s name is %s" % (Person.name, nico.name))
