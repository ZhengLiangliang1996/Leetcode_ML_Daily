#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab = a * b // math.gcd(a, b)
        lcm_ac = a * c // math.gcd(a, c)
        lcm_bc = b * c // math.gcd(b, c)
        lcm_abc = a * lcm_bc // math.gcd(a, lcm_bc)
    
        def isEnough(num):
            cnt = num // a + num // b + num // c \
                    - num // lcm_ab - num // lcm_ac - num // lcm_bc \
                    + num // lcm_abc
            return cnt >= n
            
        left, right = 1, 10**10
        while left < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                right = mid
            else:
                left = mid + 1
        return left
