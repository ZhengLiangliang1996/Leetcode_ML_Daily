#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        res = 0 
        while target > 1:
            if target & 1 == 1: # ood 
                target -= 1
                res += 1
            elif maxDoubles:
                res += 1
                target //= 2
                maxDoubles -= 1
            else:
                res += target - 1
                break 
        
        return res 
