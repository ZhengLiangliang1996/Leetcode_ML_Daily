#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        
        cur = intervals[0]
        res.append(cur)

        for nxt in intervals[1:]:
            _, cur_end = cur
            nxt_stt, nxt_end = nxt[0], nxt[1]
            
            if cur_end >= nxt_stt:
                cur[1] = max(cur_end, nxt_end)
            else:
                cur = nxt 
                res.append(cur)
        
        return res 
