#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def closest_divisors_util(X):
            # binary search 
            # odd 27 3*9 
            # odd 28 4*7 12*4
            # 1) Take the square root of the number X; we'll call it N.
            # 2) Set N equal to the ceiling of N (round up to the nearest integer).
            # 3) Test for (X % N). If N divides evenly into X, we found our first number.
            #   if 0, divide X by N to get M. M and N are our numbers
            #   if not 0, increment N by 1 and start step 3 over.
            n = math.ceil(sqrt(X))
            while X % n != 0:
                n -= 1
            
            return [X//n, n]
        
        d1 = closest_divisors_util(num+1)
        d2 = closest_divisors_util(num+2)
        
        return d1 if abs(d1[0]-d1[1]) < abs(d2[0]-d2[1]) else d2
