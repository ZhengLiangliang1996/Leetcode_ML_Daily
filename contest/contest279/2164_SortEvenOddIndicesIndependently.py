#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         nums_even, nums_odd = [], []
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 nums_even.append(nums[i])
#             else:
#                 nums_odd.append(nums[i])
            
#         nums_even.sort()
#         nums_odd.sort(reverse=True)
#         print(nums_even)
#         res = []
#         even_idx, odd_idx = 0, 0 
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 nums[i] = nums_even[even_idx]
#                 even_idx += 1
#             else:
#                 nums[i] = nums_odd[odd_idx]
#                 odd_idx += 1
        
#         return nums 
        even = sorted(nums[::2])
        odd = sorted(nums[1::2], reverse=True)
        nums[::2] = even
        nums[1::2] = odd
        return nums 
