#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
from sortedcontainers import SortedList

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        SList, ans = SortedList(), []
        for num in nums[::-1]:
            ind = SortedList.bisect_left(SList, num)
            ans.append(ind)
            SList.add(num)
            
        return ans[::-1]
