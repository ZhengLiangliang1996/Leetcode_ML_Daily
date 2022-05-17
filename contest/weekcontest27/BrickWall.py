#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for w in wall:
            for i in range(len(w)-1):
                # don't need to care about the final one
                if i == 0:
                    cnt[w[i]] += 1
                else:
                    w[i] = w[i] + w[i-1]
                    cnt[w[i]] += 1

        if len(cnt.keys()) == 0: return len(wall)
        return len(wall) - max(cnt.values())
                    
