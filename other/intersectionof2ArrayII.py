#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i] < nums2[j]:
                i = i + 1
            elif nums1[i] == nums2[j]:
                n.append(nums1[i])
                i = i + 1
                j = j + 1
            elif nums1[i] > nums2[j]:
                j = j + 1
        return n
        
