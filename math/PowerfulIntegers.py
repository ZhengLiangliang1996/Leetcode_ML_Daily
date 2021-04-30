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
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        from itertools import product
        if bound == 0:
            return []
        if x > 1:
            x_pow = range(0, int(math.log(bound, x))+1)
        else:
            x_pow = [0, 1]

        if y > 1:
            y_pow = range(0, int(math.log(bound, y))+1)
        else:
            y_pow = [0, 1]

        return {x**i + y**j for i, j in product(x_pow, y_pow) if x**i + y**j <= bound}
def main():
    pass


if __name__ == "__main__":
    main()

