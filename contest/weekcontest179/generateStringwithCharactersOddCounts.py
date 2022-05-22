#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return 'a'
        if n & 1 == 0:
            return 'a'*(n-1) + 'b'
        else:
            # odd 7: 1 + 1 + 1 + 1 + 3 
            return 'a'*(n-2) + 'b' + 'c'
