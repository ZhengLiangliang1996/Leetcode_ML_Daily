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
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        '''
        从瘦子到胖子，这样我们才能快速的知道当前最重和最轻的人。然后使用双指针，left 指向最瘦的人，right 指向最胖的人，当 left 小于等于 right 的时候，进行 while 循环。在循环中，胖子是一定要上船的，所以 right 自减1是肯定有的，但是还是要看能否再带上一个瘦子，能的话 left 自增1。然后结果 res 一定要自增1，因为每次都要用一条船.
        '''
        people.sort()
        res = 0
        n = len(people)
        l = 0
        r = n - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res += 1

        return res
def main():
    pass


if __name__ == "__main__":
    main()

