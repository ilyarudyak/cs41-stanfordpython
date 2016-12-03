#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:39:40 2016

@author: ilyarudyak
"""

def is_alphab_order_str(s):
    return s == ''.join(sorted(s))
    
    
def is_alphab_order_list(l):
    return l == sorted(l)   
               

def cyclon_order_helper(l, s, start):
    if not s:
        return l
    l.append(s[start])
    if start == 0:
        return cyclon_order_helper(l, s[1:], -1)
    else:
        return cyclon_order_helper(l, s[:-1], 0)

        
def cyclon_order(s):
    return  cyclon_order_helper([], s, 0)     
    
    
def is_cyclone_phrase(text):
    for s in text.split(' '):
        if not is_alphab_order_list(cyclon_order(s)):
            return False
    return True        
    

def is_cyclone_phrase2(text):
    return all([is_alphab_order_list(cyclon_order(s)) for s in text.split(' ')])  
    
            
print(is_cyclone_phrase2("adjourned"))
print(is_cyclone_phrase("settled"))
print(is_cyclone_phrase("all alone at noon"))
print(is_cyclone_phrase("by myself at twelve pm"))
print(is_cyclone_phrase("acb"))
print(is_cyclone_phrase(""))














