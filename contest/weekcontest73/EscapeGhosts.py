#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        if target == [0, 0]:
            return True 
    
        # just to ensure the distance between you to 
        # the target is less than every other ghosts
        d = abs(target[0]) + abs(target[1])
        
        for g in ghosts:
            gd = abs(target[0] - g[0]) + abs(target[1] - g[1])
            if d >= gd: # action happens simultaneously
                return False 
        return True 
