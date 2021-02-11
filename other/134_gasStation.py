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
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        n = len(gas)

        def isCircle(gas, cost, i):
            tank = 0
            for step in range(n):
                sta = (i + step) % n
                tank = tank + gas[sta] - cost[sta]
                if tank < 0:
                    return False

            return True

        for i in range(n):
            if gas[i] >= cost[i]:
                if isCircle(gas, cost, i):
                    return i
        return -1
def main():
    pass


if __name__ == "__main__":
    main()

