#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # left boundry 
        l = 1 
        r = n + 1
        while l < r:
            mid = l + ((r - l ) >> 1)
            
            if isBadVersion(mid):
                r = mid 
            else:
                l = mid + 1
        
        return l 
            
