#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def solve(self, data):
        products = [1 for _ in range(len(data))]
        lp = [1 for _ in range(len(data))]
        rp = [1 for _ in range(len(data))]

        l_running = 1
        for i in range(len(data)):
            lp[i] = l_running
            l_running *= data[i]
        r_running = 1
        for i in reversed(range(len(data))):
            rp[i] = r_running
            r_running *= data[i]

        for i in range(len(data)):
            products[i] = lp[i] * rp[i]

        return products

s = Solution()
print(s.solve([1, 2, 3, 4 ,5]))
