#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        def chk(idx, e):
            for i in range(len(nums)):
                if nums[(idx+i)%len(nums)] > e:
                    return nums[(idx+i)%len(nums)]
            return -1
        
        for idx, i in enumerate(nums):
            res.append(chk(idx, i))
        return res 
