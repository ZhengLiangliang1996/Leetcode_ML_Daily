#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def memLeak(self, m1, m2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """

        t = 1 
        while m1 >= t or m2 >= t:
            if m1 >= m2:
                m1 -= t
            else:
                m2 -= t
            t += 1
        return [t, m1, m2] 
