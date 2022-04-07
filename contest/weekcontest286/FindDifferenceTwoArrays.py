#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res1, res2 = [], []
        inter = list(set(nums1).intersection(set(nums2)))
        res1 = set([x for x in nums1 if x not in inter])
        res2 = set([x for x in nums2 if x not in inter])
        
        return [res1, res2]
