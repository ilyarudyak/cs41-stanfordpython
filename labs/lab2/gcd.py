#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:45:15 2016

@author: ilyarudyak
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)    
    
print(gcd(18, 84))


def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a    
    
print(gcd2(18, 84))