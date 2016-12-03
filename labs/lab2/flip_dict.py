#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:53:35 2016

@author: ilyarudyak
"""
from collections import defaultdict


def flip_dict(d):
    d_flipped = {}
    for (key, value) in d.items():
        d_flipped[value] = d_flipped.get(value, []) + [key] 
    return d_flipped    

print(flip_dict({"CA": "US", "NY": "US", "ON": "CA"}))


def flip_dict2(d):
    d_flipped = {}
    for (key, value) in d.items():
        d_flipped.setdefault(value, []).append(key)
    return d_flipped    
    
print(flip_dict2({"CA": "US", "NY": "US", "ON": "CA"}))


def flip_dict3(d):
    d_flipped = defaultdict(list)
    for (key, value) in d.items():
        d_flipped[value].append(key)
    return dict(d_flipped)

print(flip_dict3({"CA": "US", "NY": "US", "ON": "CA"}))    

















