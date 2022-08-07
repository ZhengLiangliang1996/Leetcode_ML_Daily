#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        for i in range(len(items1)):
            d[items1[i][0]].append(items1[i][1])
        
        for i in range(len(items2)):
            d[items2[i][0]].append(items2[i][1])
            
        res = []
        if not d:
            return res 
        
        for sub in d.keys():
            res.append([sub, sum(d[sub])])
        
        res.sort()
    
        return res 
