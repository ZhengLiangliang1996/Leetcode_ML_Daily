#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        cnt = collections.Counter(s)
        res = ""
        h = []
        for c in cnt.keys():
            heapq.heappush(h, [-ord(c), cnt[c]])
        
        while h:
            cur = heapq.heappop(h)
            if cur[1] <= repeatLimit:
                res += chr(-cur[0]) * cur[1]
            else:
                # first add repeatLimit 
                res += chr(-cur[0]) * repeatLimit 
                cur[1] -= repeatLimit
                if h:
                    # take one out 
                    cur2 = heapq.heappop(h)
                    res += chr(-cur2[0])
                    cur2[1] -= 1
                    heapq.heappush(h, cur)
                    if cur2[1] > 0:
                        heapq.heappush(h, cur2)
        return res 
                
