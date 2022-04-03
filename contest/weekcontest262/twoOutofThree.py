#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        res = []
        n1, n2, n3 = set(nums1), set(nums2), set(nums3)
        a, b, c = n1.intersection(n2), n1.intersection(n3), n2.intersection(n3)
        return list(a.union(b).union(c))

        
