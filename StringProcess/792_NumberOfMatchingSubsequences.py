#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # TLE 
        '''
        def checkSubsequence(s1, s2, n1, n2):
            if n1 == 0:
                return True 
            if n2 == 0:
                return False
            
            if s1[n1 - 1] == s2[n2 - 1]:
                return checkSubsequence(s1, s2, n1-1, n2-1)
            
            return checkSubsequence(s1, s2, n1, n2-1)
        res = 0
        n = len(s)
        for word in words:
            res += checkSubsequence(word, s, len(word), n)
            
        return res 
        '''
        def isSubsequence(word):
            curr = 0
            for w in word:
                idx = bisect_left(places[w], curr)
                if idx >= len(places[w]):
                    return False 
                curr = places[w][idx] +  1
            return True 
        
        places = defaultdict(list)
        for i, symbol in enumerate(s):
            places[symbol].append(i)
        
        return sum(isSubsequence(word) for word in words)
