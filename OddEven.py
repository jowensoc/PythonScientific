#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:22:02 2024

@author: john.owens
"""

myList = []

def calcOddEven(val):
    result = 0
    if val % 2 == 0:
        result = val / 2
    elif val % 2 == 1:
        result = (val * 3) + 1
   
    return result
    
    
    
for i in range(1, 11):
    myList.append(calcOddEven(i))
    
print(myList)