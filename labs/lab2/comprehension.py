#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:50:39 2016

@author: ilyarudyak
"""

#x = [2 * n + 1 for n in [0, 1, 2, 3]]
#print(x)
#
#x = [n % 3 == 0 for n in [3, 5, 9, 8]]
#print(x)
#
#S = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
#x = [s.replace("TA_", "") for s in S if s.count("TA_") > 0]
#print(x)

S = ['apple', 'orange', 'pear']
x = [s[0].upper() for s in S]
print(x)

x = [s for s in S if s.count('p') > 0] 
print(x)

x = [(s, len(s)) for s in S]
print(x)    

x = {s: len(s) for s in S}
print(x)  