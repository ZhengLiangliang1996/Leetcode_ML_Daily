#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def finalValueAfterOperations(self, os):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for o in os:
            if '++' in o:
                res += 1
            else:
                res -= 1
        return res
