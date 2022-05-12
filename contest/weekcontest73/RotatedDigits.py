#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n+1):
            tmp = set(str(i))
            if (tmp - {'1', '0', '8'}) and not tmp & {'3', '7', '4'}:
                res += 1
        return res
