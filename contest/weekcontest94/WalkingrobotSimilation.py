#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # North means +Y direction.
        # East means +X direction.
        # South means -Y direction.
        # West means -X direction.
        d_r = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        g_x, g_y = 0, 0
        m = 0
        d = 0
        os = {(ob[0], ob[1]) for ob in obstacles}
        for c in commands:
            if c == -1:# turn right
                d = (d + 1) % 4
            elif c == -2:# turn left
                d = (d - 1) % 4
            else:
                newX, newY = 0, 0
                if d_r[d][0]:
                    for _ in range(c):
                        newX = g_x+1 if d_r[d][0] == 1 else g_x-1
                        if (newX, g_y) in os:
                            break
                        g_x = newX 
                elif d_r[d][1]:
                    for _ in range(c):
                        newY = g_y+1 if d_r[d][1] == 1 else g_y-1
                        if (g_x, newY) in os:
                            break
                        g_y = newY

            m = max(g_x ** 2 + g_y** 2, m)
    
        return m
            
                
                
