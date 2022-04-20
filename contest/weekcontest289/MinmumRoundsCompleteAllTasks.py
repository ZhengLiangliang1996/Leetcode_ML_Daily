#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        res = 0
        import collections
        cnt = collections.Counter(tasks)
        for k in cnt.keys():
            if cnt[k] == 1:
                return -1
            if cnt[k] == 2 or cnt[k] == 3:
                res += 1
            else:
                if cnt[k] % 3 != 1:
                    res += (cnt[k] // 3) + ((cnt[k] % 3) // 2)
                else:
                    res += (cnt[k] // 3) - 1 + 2 
                
        return res 
