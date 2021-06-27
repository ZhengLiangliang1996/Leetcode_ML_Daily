#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Greedy 
        n = len(ratings)
        # at leat 1 for each child 
        res = [1] * n
        # 1: left to right, the right one will have one more candy than the left one if taller.
        for i in range(1, n):
            if ratings[i] > ratings[i-1]: res[i] = res[i-1] + 1
        # 2: right to left, the left one will be at least one more candy than the right one if taller.
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]: res[i] = max(res[i], res[i + 1] + 1)
                
        return sum(res)
        
