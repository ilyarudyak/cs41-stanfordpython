#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:09:47 2016

@author: ilyarudyak
"""

chain_len_map = {}

def chain_len_helper(acc, start, n):
    if n == 1:
        chain_len_map[start] = acc
        return acc
    if n in chain_len_map:
        chain_length = acc + chain_len_map[n] - 1
        chain_len_map[start] = chain_length
        return chain_length
    if n % 2 == 0:
        return chain_len_helper(acc + 1, start, n / 2)
    else:
        return chain_len_helper(acc + 1, start, 3 * n + 1)

        
def chain_len(n):
    return chain_len_helper(1, n, n)
        

def collatz(limit):
    max_len = 0
    number = 0
    for n in range(1, limit):
        collatz_len = chain_len(n)
        if collatz_len > max_len:
            number, max_len = n, collatz_len
    return number, max_len

print(collatz(limit=1000))


def collatz2(limit):
    return max(map(chain_len, range(1, limit)))
    
print(collatz2(limit=1000))    















