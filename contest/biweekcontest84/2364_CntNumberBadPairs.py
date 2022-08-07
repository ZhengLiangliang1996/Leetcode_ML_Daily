#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countBadPairs(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(a)
        cnt = 0 
        mp = collections.defaultdict(int)
        for i in range(n):
            cnt += mp[i-a[i]]
            mp[i-a[i]] += 1
        return n * (n-1)/2 - cnt
