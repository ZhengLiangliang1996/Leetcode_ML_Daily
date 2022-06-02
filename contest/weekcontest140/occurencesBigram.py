#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        if (first + ' ' + second) not in text:
            return []
        l = text.split(' ')

        for i in range(len(l)-2):
            if l[i] == first and l[i+1] == second:
                if l[i+2]:
                    res.append(l[i+2])
        return res 
            
