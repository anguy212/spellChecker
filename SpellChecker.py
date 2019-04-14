#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:08:31 2019

@author: alicenguyen
"""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = ""
corpus = ""
with open('mobydick.txt', 'r') as f:
    text = f.readlines()
    text = map(lambda x: x.strip(), text)
    corpus = "\n".join(text)
    
stopW = set(stopwords.words('english'))
tokenizedW = word_tokenize(corpus)
final = []

holder = ""
prev = ""
for w in tokenizedW:
    if w not in stopW:
        if holder == "":
            if w[len(w)-1] == '-':
                holder = w[0:len(w)-1]
            else:
                final.append(w)
                prev = w
        else:
            w = holder + w
            final.append(w)
            holder = ""
print(final)
#AFTER THIS SECTION, FINAL WILL CONTAIN LIST OF WORDS IN MOBY DICK
#SOME WORDS WILL BE "-LINES" INDICATING IT IS ENDING HYPHENATE OF WORD
#SOME WORDS WILL BE "WHALE-BOAT" INDICATING IT IS HYPHENATE



