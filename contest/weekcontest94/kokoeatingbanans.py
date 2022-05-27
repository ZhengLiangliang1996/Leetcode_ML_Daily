#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        # 思路 H在1和max（piles）猜测 
        l, r = 1, max(piles)+1
        
        while(l < r):
            curH = 0
            mid = l + ((r - l) >> 1)
            
            for i in piles:
                curH += i // mid + (1 if i % mid else 0)
                #curH += math.ceil(i / mid)
            
            # 大于H 证明花的时间太多的 则需要每分钟吃得更多 注意这里是和之前相反的思维 因为mid作用是反的
            if curH > H:
                l = mid + 1
            # 小于等于H 证明花的时间少 每分钟吃多了 减小需要吃的个数 
            else:
                r = mid 
        
        return l
