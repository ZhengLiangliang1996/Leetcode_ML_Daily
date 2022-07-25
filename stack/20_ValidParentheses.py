#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '': return True 
        d = {'[':']', '(':')', '{':'}'}
        stack = []
        for i in range(len(s)):
            if s[i] == ']' or s[i] == ')' or s[i] == '}':
                if not stack:
                    return False 
                else:
                    a = stack.pop()
                    if d[a] != s[i]:
                        return False
            else:
                stack.append(s[i])
        
        return len(stack) == 0
