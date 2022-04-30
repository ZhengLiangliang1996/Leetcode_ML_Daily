#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = []
        for sub in s.split(" "):
            tmp.append([sub[-1], sub[:-1]])
        
        tmp.sort()
        
        return ' '.join([x[1] for x in tmp])
