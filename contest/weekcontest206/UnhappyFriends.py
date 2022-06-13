#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def unhappyFriends(self, n: int, perf: List[List[int]], p: List[List[int]]) -> int:
        res = set()
        
        pd = {}
        for i in p:
            pd[i[0]] = i[1]
            pd[i[1]] = i[0]

        def chk(x, y):
            yind = perf[x].index(y) 
            if yind == 0:
                return False
            
            yind -= 1
            while yind >= 0:
                u = perf[x][yind]
                v = pd[u] 
                if perf[u].index(v) > perf[u].index(x):
                    return True
                yind -= 1
            
            
            return False
        for i in range(len(p)):
            if chk(p[i][0], p[i][1]):
                
                res.add(p[i][0])
            if chk(p[i][1], p[i][0]):
                
                res.add(p[i][1])
        
        return len(res) 
