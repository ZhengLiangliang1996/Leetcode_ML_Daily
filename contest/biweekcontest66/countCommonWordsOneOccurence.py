#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        res = 0
        import collections
        cnt1 = collections.Counter(words1)
        cnt2 = collections.Counter(words2)
        for k in cnt1.keys():
            if cnt1[k] == 1:
                if cnt2[k] == 1:
                    res += 1
        
        return res 
