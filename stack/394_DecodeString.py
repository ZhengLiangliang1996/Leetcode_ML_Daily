#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return s 
        digit_s = []
        str_s = []
        res = ""
        temp_num = 0
        for i in range(len(s)):
            if s[i] == '[':
                digit_s.append(temp_num)
                str_s.append(res)
                res = ""
                temp_num = 0
            elif s[i] == ']':
                pre_num = digit_s.pop()
                pre_str = str_s.pop()
                res = pre_str + pre_num * res
            elif s[i].isdigit():
                temp_num = temp_num*10 + int(s[i])
            else:
                res += s[i]

        return res 
