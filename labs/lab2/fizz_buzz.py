#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:42:09 2016

@author: ilyarudyak
"""

# Find the sum of all the multiples of 3 or 5 below 1001


def find_sum(limit):
    sum_of_mult = 0
    for n in range(limit):
        if (n % 3 == 0) or (n % 5 == 0):
            sum_of_mult += n
    return sum_of_mult
    
print(find_sum(1001))        


def find_sum2(limit):
    return sum([n for n in range(limit) if (n % 3 == 0) or (n % 5 == 0)])    

print(find_sum2(1001)) 

    
def find_sum3(limit):
    return sum(filter(lambda n: (n % 3 == 0) or (n % 5 == 0), range(limit)))
    
print(find_sum3(1001))



















     