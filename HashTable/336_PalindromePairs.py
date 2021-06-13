#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ''' TLE 
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    combine = words[i] + words[j]
                    if combine[::-1] == combine:
                        res.append((i, j))
        return res 
        '''
        # condition 
        # len(w1)==len(w2) and the reversed w1 equals w2
        # len(w1)>len(w2) and the w1 must start with the reversed w2 and the remaining part of w1 should be a palindrome itself
        # len(w1)<len(w2) and w2 must end with the reversed w1 and the remaining part of w2 should be a palindrome itself
        rmap={w[::-1]:i for i,w in enumerate(words)}
        
        res=[]
        for i,wrd in enumerate(words):
            rev=wrd[::-1]
            if wrd in rmap:                        # same length pair
                if rmap[wrd]!=i:                   # i and j should be distinct
                    res.append((i,rmap[wrd]))
            for j in range(1,len(wrd)+1):          # first or last j characters as palindrome, other part has pair
                if wrd[:-j] in rmap and wrd[-j:]==rev[:j]:
                    res.append((i,rmap[wrd[:-j]]))
                if wrd[j:] in rmap and wrd[:j]==rev[-j:]:
                    res.append((rmap[wrd[j:]],i))
        return res
