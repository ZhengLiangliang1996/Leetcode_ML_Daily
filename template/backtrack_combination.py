#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
class Solution(object):
    def combinationSum2(self, c, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, target, stt):
            if target == 0:
                res.append(path)
                return

            for i in range(stt, len(c)):
                # prune
                if c[i] > target: return
                if i > stt and c[i] == c[i-1]:
                    continue
                dfs(path + [c[i]], target-c[i], i+1)

        c.sort()
        dfs([], t, 0)
        return res


    def combinationSum(self, c, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, target, stt):
            if target == 0:
                res.append(path)
                return
    
            # choice 
            for i in range(stt, len(c)):
                # prune 
                if c[i] > target: return 
                dfs(path+[c[i]], target-c[i], i)
        
        c.sort()
        dfs([], target, 0)
        return res 

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        res = []
        dig_dict = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        def backtrack(path, start):
            if len(path) == len(digits):
                res.append(path)

            for i in range(start, len(digits)):
                for j in dig_dict[digits[i]]:
                    backtrack(path+j, i + 1)

        backtrack('', 0)
        return res

def main():
    pass


if __name__ == "__main__":
    main()

