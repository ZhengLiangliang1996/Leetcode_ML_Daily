#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1

        while r < len(prices):
            cur = prices[r] - prices[l]
            if prices[l] < prices[r]: 
                res = max(res, cur)
            else:
                l = r 
            r += 1
        
        return res 
