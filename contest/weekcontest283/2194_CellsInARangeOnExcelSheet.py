#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        a,b = s.split(":")
        for i in range(ord(a[0]), ord(b[0])+1):
            for j in range(int(a[1]), int(b[1])+1):
                res.append(chr(i)+str(j))
        
        return res 
