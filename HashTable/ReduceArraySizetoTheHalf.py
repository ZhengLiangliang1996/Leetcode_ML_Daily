#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        c = Counter(list(arr))
        res = 0
        n1 = len(arr)
        mid = n1 // 2
        for k,v in c.most_common():
            n1 -= v
            res += 1
            if n1 <= mid:
                break
        
        return res
