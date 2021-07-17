#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def threeEqualParts(self, A):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Inspired by DBabichev

        n = len(A)
        # 1. check all the places, where we have 1. Let us have m elements such that.
        indexes = [i for i in range(n) if A[i] == 1]
        m = len(indexes)
        
        if m == 0: return [0, 2]
        if m % 3 != 0: return [-1, -1]
        # 2. Let us find now 6 indexes: p1, p2, p3, p4, p5, p6
        # p1 is index of first 1
        # p2 is index of last one in first part
        # p3 is index of fisrt one in second part, and so on 
        # Then it is necessary that A[p1:p2+1] equal to A[p3:p4+1] equal to A[p5:p6+1]
        # Note that is is not sufficient though, because we can add some zeroes in the ends. So, if this condition do not holds, we return [-1, -1].
        p1, p2 = indexes[0], indexes[m//3-1]
        p3, p4 = indexes[m//3], indexes[2*m//3-1]
        p5, p6 = indexes[2*m//3], indexes[-1]
        part1, part2, part3 = A[p1:p2+1], A[p3:p4+1], A[p5:p6+1]
        if part1 != part2 or part2 != part3: return [-1, -1]
        
        # Evaluate lengths of how many zeros we can add in the end: l1, l2, l3. For l3 we do not 
        # have any choice: we need to take all there zeroes. For l1 and l2 we can put zeroes in 
        # the beginning of one number or to the end of the next, so the options we have are: 
        # [0, ..., l1] for the first, [0, ..., l2] for the second and [l3] for third. 
        # So, if l3 > l2 or l3 > l1, we can not make parts equal and we return [-1, -1].
        
        l1 = p3 - p2 - 1
        l2 = p5 - p4 - 1
        l3 = n - p6 - 1
        
        if l3 > l2 or l3 > l1: return [-1, -1]
        
        return [p2 + l3, p4 + l3 + 1]
