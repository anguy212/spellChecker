#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:04:08 2019

@author: alicenguyen
"""

longest = ""
with open('mobydick_snt/tokens.txt') as f:
    text = f.readlines()
    for line in text:
        for word in line.split():
            if len(word) > len(longest):
                longest = word
                
print(longest)

