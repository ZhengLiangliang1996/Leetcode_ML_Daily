#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re 
        pattern = re.compile('\d+')
        res = float('-inf')
        for i in pattern.findall(s):
            if int(i) > res:
                res = int(i)
            else:
                return False
        return True
              
