#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        if f is [] or s is []:
            return []
        # left: find the max 
        # right: find the min 
        # next starting point: min(right)
        res = []
        n, m = len(f),  len(s)
        i, j = 0, 0 
        while i < n and j < m:
            # left
            leftMax = max(f[i][0], s[j][0])
            # right
            rightMin = min(f[i][1], s[j][1])
            
            # next starting point 
            if s[j][1] > f[i][1]:
                i += 1
            else:
                j += 1
            if leftMax <= rightMin:
                res.append([leftMax, rightMin])
        
        return res 
