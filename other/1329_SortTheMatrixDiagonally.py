#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        In this problem we are asked to sort each diagonal, so it is good idea to traverse all matrix and create defaultdict d: numbers on each diagonal. Note, that inside each diagonal j - i is the same, so it can be used as key for our defaultdict. There will be two stages:

Traverse over all matrix and put mat[i][j] to the end of d[j - i].
Sort each diagonal and put values back to matrix mat. There is a small trick: imagine that k is value of j - i on diagonal, than j = i + k, so we need to update cell with cooridinates (i, i + k). However we need to be careful here: we can have negative indexes, so if k is negative, we need to start not from k, but from 0, that is add -k. In general indexes can be written as ([i + max(-k, 0), k + i + max(-k, 0)): for positive k it is just (i, k + i) and for negative it is (i - k, i).
Complexity: time complexity is O(mn*log(min(m,n)), because we have O(m+n) diagonals on each no more than min(m,n) elements we need to sort. Space complexity is O(mn).
        '''
        m = len(mat)
        n = len(mat[0])

        if m == 1 or n == 1:
            return mat
        # store the #[j-i] of diagonal in a list in the dict, key is the index j - i
        d = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[j - i].append(mat[i][j])

        for k in d:
            for i, num in enumerate(sorted(d[k])):
                mat[i + max(-k, 0)][k + i + max(-k, 0)] = num

        return mat






def main():
    pass


if __name__ == "__main__":
    main()

