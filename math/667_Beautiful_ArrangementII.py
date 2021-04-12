#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

# TLE
class Solutioni1(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        n_list = [i for i in range(1, n+1)]

        if k == 1:
            return n_list

        def distinct_integer(elms):
            res = []
            for i in range(1, len(elms)):
                res.append(abs(elms[i] - elms[i-1]))

            return k == len(set(res))



        used = [0] * len(n_list)
        res = []
        def backtrack(path):
            if len(res) >= 1:
                return

            if len(path) == len(n_list):
                if distinct_integer(path):
                    res.append(path)
                    return

            for i in range(len(n_list)):
                if used[i]: continue

                used[i] = 1
                backtrack(path+[n_list[i]])
                used[i] = 0

        backtrack([])
        return res[0]


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        '''
        Just create sentence 1,2, . . . , n−k, n, n−k+ 1, n−1, . . ., where we start to take biggest and smallest elements from place n−k. Let us consider case n = 14 and k = 6, then what [1,2,3,4,5,6,7,8,14,9,13,10,12,11]: then first differences are equal to 1, then we have differencese 6, -5, 4, -3, 2, -1, so in the end we will have absolute differences 1, 2, 3, 4, 5, 6.

Complexity
Time complexity is O(n), space as well to form output array
        '''

        dr, diff = 1, k
        result = list(range(1, n-k+1))
        for i in range(k):
            result.append(result[-1] + dr*diff)
            dr *= -1
            diff -= 1
        return result



def main():
    s = Solutioni1()
    #ans1 = s.constructArray(92, 80)
    #print(ans1)


if __name__ == "__main__":
    main()

