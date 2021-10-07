#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air.localdomain>
#
# Distributed under terms of the MIT license.
# The guess API is already defined for you.
# @param num, your guess
# @# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        
        while l <= r:
            mid = l + (r-l) // 2
            
            if guess(mid) == -1:
                r = mid-1
            elif guess(mid) == 1:
                l = mid+1                
            else:
                return mid
        return mid
