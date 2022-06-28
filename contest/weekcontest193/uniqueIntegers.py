#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        cnt = collections.Counter(arr)
        res = len(cnt.most_common())

        for i,j in cnt.most_common()[::-1]:
            if k >= j:
                k -= j
                res -= 1
                
            else:
                return res 
        return 0
