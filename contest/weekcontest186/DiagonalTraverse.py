#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # heap 
        import heapq
        heap = []
        res = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heap.append([i+j, j, i])
    
        heapq.heapify(heap)
        
        while heap:
            _, j, i = heapq.heappop(heap)
            res.append(nums[i][j])
        
        return res 
