#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        sort_s, final_s = '', ''
        for i in s:
            if i in order:
                sort_s += i
            else:
                final_s += i
        if sort_s != '':
            sort_s = ''.join(sorted(sort_s, key=lambda word: [order.index(c) for c in word]))
        return sort_s + final_s
        
