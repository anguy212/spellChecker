#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:27:10 2019

@author: rocioroman
"""
from nltk.corpus import words

def longestComSubSeq(X, Y, m, n):
    L = [[None]*(n+1) for i in range(m+n)]
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
    return L[m][n]
    

'''X = "iangle"
Y = "trilingle"
print("LCS is ", longestComSubSeq(X,Y,len(X),len(Y)))'''


def returnLCSrecs(mispelled):
    word_list = words.words()
    lcsDic = {}
    holder = 0
    highest = 0;
    #mispelled = "tirangle"
    
    if len(mispelled) <= 2:
        floor = 1
    else:
        floor = len(mispelled) - 1
    cap = len(mispelled) + 1
    length = 0
    # prints 236736
    for item in word_list:
        length = len(item)
        if length >= floor and length <= cap:
            holder = longestComSubSeq(mispelled,item,len(mispelled),len(item))
            if holder >= highest:
                lcsDic[item] = holder
                highest = holder
    
    finalLis = []
    for word, number in lcsDic.items():
        if number >= highest:
            finalLis.append(word)
            
    #print(finalLis)
    return finalLis