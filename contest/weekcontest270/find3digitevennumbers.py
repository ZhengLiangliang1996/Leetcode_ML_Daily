#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = Counter(digits)
        
        res = []
        
        def backtrack(n, total):
            if n == 3:
                res.append(total)
            else:
                for num, count in counter.items():
                    if count <= 0:
                        continue
                    if not n and num == 0:
                        continue
                    if n == 2 and num % 2 != 0:
                        continue

                    counter[num] -= 1
                    n += 1
                    total *= 10
                    total += num
                    
                    backtrack(n, total)
                    
                    counter[num] += 1
                    n -= 1
                    total -= num
                    total = total // 10
                    
                    
        backtrack(0, 0)
        res.sort()
        
        return res
