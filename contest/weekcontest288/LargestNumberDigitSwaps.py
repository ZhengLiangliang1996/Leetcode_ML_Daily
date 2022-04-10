#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        li = [int(x) for x in str(num)]
        even, odd = [], []
        for i in range(len(li)):
            if li[i] & 1 == 0:
                even.append(li[i])
            else:
                odd.append(li[i])
        even.sort()
        odd.sort()
        
        res = 0 
        for i in range(len(li)):
            if li[i] & 1 == 0:
                res = res * 10 + even.pop()
            else:
                res = res * 10 + odd.pop()
        
        return res 
