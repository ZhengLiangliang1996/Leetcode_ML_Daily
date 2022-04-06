#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@MacBook-Air>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        import collections
        res = [[], []]
        if not matches: return res 
        win_li = [x[0] for x in matches]
        los_li = [x[1] for x in matches]
        
        res1 = list(set(win_li) - set(los_li))
        res2 = []
        cnt = collections.Counter(los_li)
        for k in cnt.keys():
            if cnt[k] == 1:
                res2.append(k)
        res1.sort()
        res2.sort()
        return [res1, res2]
