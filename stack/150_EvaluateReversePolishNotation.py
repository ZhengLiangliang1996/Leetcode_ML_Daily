#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s, oprs = [], ['+', '-', '*', '/']
        res = 0
        for t in tokens:
            if t in oprs:
                scd = int(s.pop())
                frd = int(s.pop())

                res = int(eval(str(frd)+t+str(scd)))
                s.append(res)
                print(str(frd)+t+str(scd),'=',str(res))
            else:
                s.append(t)
        return int(s.pop())

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

