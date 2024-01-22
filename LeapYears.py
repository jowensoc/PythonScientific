#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:45:59 2024

@author: john.owens
"""

l = [2020, 2096, 2100, 2104, 2300, 2400]

def isLeapYear(val):
    leapYearFlag = False
    if val % 400 == 0:
        leapYearFlag = True
    elif val % 100 == 0:
        leapYearFlag = False
    else:
        leapYearFlag =  val % 4 == 0
        
    filler = (" NOT ", " ")[leapYearFlag]
    
    print("{0} is{1}a Leap Year".format( val, filler))
    
    

for i in l:
    isLeapYear(i)
