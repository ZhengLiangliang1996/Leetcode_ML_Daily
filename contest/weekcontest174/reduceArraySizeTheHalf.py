#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [x[1] for x in collections.Counter(arr).most_common()]
        a, res = n, 0
        
        # Binary Search 
        l, r = 0, len(cnt)
        
        # Left Bound 
        while l < r:
            mid = l + (r - l) // 2
            # 
            if sum(cnt[:mid]) >= n//2:
                r = mid
            elif sum(cnt[:mid]) < n//2:
                l = mid + 1
                
        return l
