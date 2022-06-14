#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        def chk(idx, e):
            for i in range(idx, len(nums2)):
                if nums2[i] > e:
                    return nums2[i]
            return -1
        for i in nums1:
            idx = nums2.index(i)
            res.append(chk(idx, i))
        return res 
