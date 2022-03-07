#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimalKSum(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
#         res = 0
#         i = 0
#         while k > 0:
#             i += 1
#             if i not in nums:
#                 k -= 1
#                 res += i
        
#         return res 
        ans = (1+k)*k//2
        for v in sorted(set(A)):
            if v <= k :
                k+=1
                ans += k-v
        return ans
        
