#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimizeResult(self, e):
        """
        :type expression: str
        :rtype: str
        """
        idx = e.index('+')
        res, res_exp = float('inf'), e
        
        def evaluate(exps):
            return eval(exps.replace('(','*(').replace(')', ')*').lstrip('*').rstrip('*'))
        
        for i in range(idx):
            for j in range(idx+1, len(e)):
                exp = f"{e[:i]}({e[i:idx]}+{e[idx+1:j+1]}){e[j+1:len(e)]}"
                tmp = evaluate(exp)
                if tmp < res:
                    res = tmp 
                    res_exp = exp 
        return res_exp 
