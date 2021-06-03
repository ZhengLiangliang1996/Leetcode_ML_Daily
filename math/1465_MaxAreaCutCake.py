#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

class Solution(object):
    def maxArea(self, h, w, hcs, vcs):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        # Sort the arrays, then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.
        hcs.sort()
        vcs.sort() 
        max_hc = hcs[0]
        max_vc = vcs[0]
        
        for i in range(1, len(hcs)):
            max_hc = max(max_hc, hcs[i] - hcs[i-1])
        max_hc = max(max_hc, h - hcs[len(hcs)-1])
        for j in range(1, len(vcs)):
            max_vc = max(max_vc, vcs[j] - vcs[j-1])
        max_vc = max(max_vc, w - vcs[len(vcs)-1])
        
        return max_vc*max_hc % MOD
