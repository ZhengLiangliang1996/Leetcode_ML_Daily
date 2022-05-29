#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def discountPrices(self, s: str, d: int) -> str:
        arr = s.split()
        for i, num in enumerate(arr):
            if num[0] == '$' and num[1:].isnumeric():
                arr[i] = '$' + "{:.2f}".format(float(num[1:]) * (1 - d/100.0))
        return ' '.join(arr)
        
