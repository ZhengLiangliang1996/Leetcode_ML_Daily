#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for word in words:
            if word not in d:
                even = []
                odd = []            
                for i in range(0,len(word)):                                
                    if i %2 == 0:
                        even.append(word[i])
                    else:
                        odd.append(word[i])
                    even.sort()
                    odd.sort()
                    d[word] = [even , odd]
    
        res = []
        for word in words:
            if d[word] not in res:
                res.append(d[word])
        return len(res)
                
