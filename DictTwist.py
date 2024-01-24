#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:35:12 2024

@author: john.owens
"""
d = { "item1": 1, "item2": 2 }
d["item3"] = 3

print(d)

del d["item3"]

for key, value in d.items():
    print(key, value)