#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        t = sum(c)
        n = len(c)

        min_sum = sum(c[:n-k])
        # sliding window in remaining n-k, min, then total - sum(n-k)
        # will be the max of the res
        subarray_sum = min_sum
        for i in range(n-k, n):
            # minus the l 
            subarray_sum -= c[i - (n-k)]
            # add the r 
            subarray_sum += c[i]

            min_sum = min(min_sum, subarray_sum)
        

        return t - min_sum
