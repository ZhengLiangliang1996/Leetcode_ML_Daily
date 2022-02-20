#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# find the left max and right max and then take the min and sum up
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMax = [0] * len(height)
        lm = height[0]
        for i in range(len(height)):
            lm = max(lm, height[i])
            leftMax[i] = lm
        
        rightMax = [0] * len(height)
        rm = height[-1]

        for i in range(len(height)-1, -1, -1):
            rm = max(rm, height[i])
            rightMax[i] = rm
        
        res = 0
        for i in range(len(height)):
            res += (min(leftMax[i], rightMax[i]) - height[i])
        
        return res 
        
