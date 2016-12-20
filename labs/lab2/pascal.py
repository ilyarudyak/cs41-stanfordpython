#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 01:54:21 2016

@author: ilyarudyak
"""

def generate_pascal_row(row):
    next_row = [1] * (len(row) + 1)
    #print(next_row)
    next_row[1:-1] = [x + y for x, y in zip(row[:-1], row[1:])]
    return next_row
    
print(generate_pascal_row([1, 2, 1]))    
print(generate_pascal_row([1, 4, 6, 4, 1]))