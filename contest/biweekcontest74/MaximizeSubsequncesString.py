#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        import collections
        #cnt = collections.Counter(text)
        #print(cnt)
        res = 0
        forward, backward = 0, 0 
        b,f = 1, 1
        for i in text:
            if i == pattern[1]:
                forward += f
            if i == pattern[0]:
                f += 1
        
        for i in text[::-1]:
            if i == pattern[0]:
                backward += b
            if i == pattern[1]:
                b += 1
                
        return max(forward, backward) 
        
