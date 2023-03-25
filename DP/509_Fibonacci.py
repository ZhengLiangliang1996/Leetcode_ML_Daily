#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        fn_0, fn_1 = 0, 1
        for i in range(2, n+1):
            temp = fn_1
            fn_1 = fn_0 + fn_1
            fn_0 = temp
        
        return fn_1 
