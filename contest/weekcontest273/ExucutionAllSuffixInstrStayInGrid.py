#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        dirs = {"D":[1, 0], "U":[-1, 0], "L":[0, -1], "R":[0, 1]}
        res = [] 
        for i in range(len(s)):
            x = startPos[0]
            y = startPos[1]
            cnt = 0
            for instr in s[i:]:
                d = dirs[instr]
                x += d[0]
                y += d[1]
                if x < 0 or x >= n or y < 0 or y >= n:
                    res.append(cnt)
                    break
                if  cnt + 1 == len(s[i:]):
                    res.append(cnt+1)
                cnt += 1
        return res 
