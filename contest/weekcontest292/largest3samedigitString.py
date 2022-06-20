#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = float('-inf')
        res_s = ""
        for i in range(len(num)-3+1):
            s = num[i:i+3]

            cnt = collections.Counter(s)

            if len(cnt.keys()) == 1:
                if  int(s) > res:
                    res = int(s)
                    res_s = s
        return res_s
