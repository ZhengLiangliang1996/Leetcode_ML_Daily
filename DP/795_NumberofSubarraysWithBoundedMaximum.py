#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        # dp 以A[i]为结尾的子数组中满足题目要求的数组个数
        # 1. A[i] < L: 这个情况，以A[i]为结尾的子数组的最大值没有改变，因此dp[i] = dp[i - 1]
        # 2. A[i] > R: 此时，以A[i]为结尾的子数组的最大值已经大于了R，所以dp[i] = 0.把这个位置设定为新的开始，记录该位置为prev.
        # 3. L <= A[i] <= R: 从prev到i之间的任意起始位置到i的子数组都满足题目条件，因此dp[i] = i - prev.
        '''
        if not A:
            return 0
        dp = len(A) * [0]
        prev = -1 
        for i, num in enumerate(A):
            if num < L and i > 0:
                dp[i] = dp[i-1]
            elif num > R:
                dp[i] = 0
                prev = i
            elif L <= num <= R:
                dp[i] = i - prev
        
        return sum(dp)
        
        '''
        '''
        Let count(bound) is the number of subarrays which have all elements less than or equal to bound.
Finally, count(right) - count(left-1) is our result.
How to compute count(bound)?
Let ans is our answer
Let cnt is the number of consecutive elements less than or equal to bound so far
For index i in 0..n-1:
If nums[i] <= bound then cnt = cnt + 1
Else cnt = 0
ans += cnt // We have total cnt subarrays which end at index i_th and have all elements are less than or equal to bound
        '''
        
        def count(bound):
            cnt = res = 0
            for x in A:
                cnt = cnt + 1 if x <= bound else 0
                res += cnt
            return res
    
        return count(R) - count(L-1)
        
                
            
