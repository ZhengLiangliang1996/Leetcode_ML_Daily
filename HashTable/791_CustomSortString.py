#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        cnt = Counter(str)
        ans = ""
        for c in order:
            if cnt[c] > 0:
                ans += cnt[c] * c
                del cnt[c]
        for c, v in cnt.items():
            ans += v * c
        return ans
