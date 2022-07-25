#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    # Time:O(N^2)  Space: O(N)
    def SmallestDiff(self, num1, num2):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num1.sort()
        num2.sort()
        idx_1, idx_2 = 0, 0 
        smallest, cur = float('inf'), float('inf')
        res = []

        while idx_1 < len(num1) and idx_2 < len(num2):
            l_v, r_v = num1[idx_1], num2[idx_2]
            if num1[idx_1] == num2[idx_2]:
                return [l_v, r_v]
            elif num1[idx_1] > num2[idx_2]:
                cur = l_v - r_v 
                idx_2 += 1
            else:
                cur = r_v - l_v 
                idx_1 += 1

            if cur < smallest: 
                smallest = cur 
                res = [l_v, r_v]
        
        return res 

num1 = [-1, 5, 10, 20, 28, 3]
num2 = [26, 134, 135, 15, 17]

s = Solution()
print(s.SmallestDiff(num1, num2))
