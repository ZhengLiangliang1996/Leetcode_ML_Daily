#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        if len(set(cards)) == len(cards):
            return -1 
        d={}
        for i in range(len(cards)):
            if cards[i] in d:
                d[cards[i]].append(i)
            else:
                d[cards[i]]=[i]
        
        res = float('inf')

        for k in d.keys():
            if len(d[k]) > 1:
                for i in range(len(d[k])-1):
                    res = min(res, d[k][i+1] - d[k][i] + 1)
        
        return res 
