#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for n in nums:
            sub = ""
            for nn in str(n):
                sub += str(mapping[int(nn)])
            d[int(sub)].append(n)
        
        l_k_s = list(d.keys())
        l_k_s.sort()
        res = [] 
        for l in l_k_s:
            res.extend(d[l])
        
        return res 
        
       
        
        
