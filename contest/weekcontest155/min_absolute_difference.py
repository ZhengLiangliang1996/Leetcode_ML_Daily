#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        gap, res = [], []
        arr.sort()
        for i in range(1, len(arr)):
            gap.append(arr[i] - arr[i-1])
        
        min_ele = min(gap)
        for i in range(len(gap)):
            if gap[i] == min_ele:
                res.append([arr[i], arr[i+1]])
        
        return res 
                
