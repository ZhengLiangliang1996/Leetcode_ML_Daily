#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        d = collections.defaultdict(list)
        for s in strs: 
            sub = []
            s_c = ''.join(sorted(s))
            #if not d.get(s_c):
            d[s_c].append(s)
        
        for _, v in d.items():
            res.append(v)
        
        return res 
