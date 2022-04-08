#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def interchangeableRectangles(self, r):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        res = 0
        import collections
        cnt = collections.Counter([x[0]/float(x[1]) for x in r])
        for k in cnt.keys():
            res += (cnt[k] * (cnt[k] - 1)) // 2
        return res 
