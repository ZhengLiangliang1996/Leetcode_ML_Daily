#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import collections
        cnt = collections.Counter(s)
        res = -1 
        for k in cnt.keys():
            if res == -1:
                res = cnt[k]
            else:
                if res != cnt[k]:
                    return False
        return True 
            
