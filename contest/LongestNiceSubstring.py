#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1: return ""

        def chk(sub):
            for i in sub:
                if chr(ord(i) ^ ord(' ')) not in sub:
                    return False 
            return True 
        
        maxLen = ""
        for i in range(len(s)):
            for j in range(len(s), i+1, -1):
                if len(s[i:j]) > len(maxLen) and chk(s[i:j]):
                    maxLen = s[i:j]

        
        return maxLen
        
