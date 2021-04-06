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
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Odd case: consider 1, 3, 5, 7, 9, 11, 13, 15, 17 to see the pattern. Then we need to make all numbers equal to 9. How many operations we need? For pair 7,11 we need 2 operations, for 5,13 we need 4 operation, then 6 and 8. In total we need 2+4+6+8 = 20 operations. How to calculate it in general case? If n = 2k + 1, then we need to calculate 2 + 4 + ... + 2k, which is the sum of arithmetic progression and equal to k*(k+1) = (n*n-1)//4.
Even case: consider 1, 3, 5, 7, 9, 11, 13, 15 to see the pattern. Then we need to make all numbers equal to 8. We need 1 + 3+ 5 + 7 = 16 operations and in general case we need 1 + 3 + ... + 2k-1 = k*k = n*n//4 operations.
Finally we can write down it as one formula, using rounding.
        '''

        return n*n//4

if __name__ == "__main__":
    main()

