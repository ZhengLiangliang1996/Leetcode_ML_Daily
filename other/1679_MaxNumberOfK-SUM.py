#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
'''
The question which is asked: how many pairs can be constructed, such that sum in each pair is equal to k. Imagine, that k = 8 and we have numbers 2, 2, 2, 6, 6, 6, 6, 6, 6. Then we can construct 3 pairs in this case. In general if we have c1 times of number x and c2 times of number k - x, we can construct min(c1, c2) pairs with numbers x, k - x. So, all we need to do is to use Counter(nums) to calculate frequency of each number and then iterate over each number val, try to find number equal to k - val and update ans by min(freq, cnt[k - val]). Note also, that when we do this, we count each pair exaclty 2 times, so we need to divide answer by 2 in the end.
'''

from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        cnt = Counter(nums)
        set_nums = list(set(nums))
        for val in cnt:
            res += min(cnt[val], cnt[k - val])
        return res // 2

    def onelinesolution():
        return (lambda c: sum(min(c[n], c[k-n]) for n in c))(Counter(nums))//2

if __name__ == "__main__":
    main()

