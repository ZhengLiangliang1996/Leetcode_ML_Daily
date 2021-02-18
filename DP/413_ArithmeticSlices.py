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
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''
        dp[i] stands for up util element i, the total number of arithmeticslices
        [1,3,5,7,9]
        dp[2] = 1
        dp[3] = dp[2] + 1 = 2
        dp[4] = dp[3] + 1 = 3

        数组	        等差数列的数目	    与上一数组的等差数列数目比较（这个目的是看转移方程）
        1 2 3	            1	                    1 - 0 = 1
        1 2 3 4	            3	                    3 - 1 = 2
        1 2 3 4 5	        6	                    6 - 3 = 3
        1 2 3 4 5 6	        10	                    10 - 6 = 4
        1 2 3 4 5 6 7	    15	                    15 - 10 = 5


        例如4个元素的arithmetic数列，子arithmetic数列个数为：
        （4-3+1）+（4-4+1）=3
        例如5个元素的arithmetic数列，子arithmetic数列个数为：
        （5-3+1）+（5-4+1）+（5-5+1）=6
        则n个元素的arithmetic数列，子arithmetic数列个数为：
        （1+n）+(n) +…+1
        也可以表达为从1加到n+1,
        代码中用num表示总的arithmetic数列的个数，consecutive表示A中某个arithmetic的长度（即上述推导的n）

        '''


        dp = [0] * len(A)
        for i in range(2, len(A)):
            if (A[i - 1] - A[i - 2] == A[i] - A[i - 1]):
                dp[i] = dp[i-1] + 1


        return sum(dp)
def main():
    pass


if __name__ == "__main__":
    main()

