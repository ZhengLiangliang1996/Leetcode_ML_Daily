#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if stack == []: 
                stack.append(i)
            elif i != stack[len(stack)-1]:
                stack.append(i)
            else:
                stack.pop()
        
        return ''.join(x for x in stack)
    
