#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0

        neg_fl = False 
        if num < 0: 
            neg_fl = True 
            num = abs(num)

        res = sorted(int(digit) for digit in str(num))

        if neg_fl:
            res = res[::-1]
        else:
            if res[0] == 0:
                i = 1
                while res[i] == 0:
                    i += 1
                res[0], res[i] = res[i], res[0]
        
        res = int("".join(str(digit) for digit in res))
        return -res if neg_fl else res 

