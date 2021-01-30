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
Let us look more carefully at this problem: how can some value be changed, let us look at several examples:
3 -> 6, 5 -> 10, 7 -> 14, that is for odd number we can have only two candidates.
2 -> 1, 4 -> 2 -> 1, 6 -> 3, 8 -> 4 -> 2 -> 1, 10 -> 5, 12 -> 6 -> 3 and so on

Now, we can reformulate our problem in the following way: we are given several lists and we need to choose candidate from each of these lists, such that deviation is minimized. This is exactly what problem 632 Smallest Range Covering Elements from K Lists is about and we can reuse the idea.

So, we have lists L1, l2, ..., Ln and let us put all smallest values from each list to heap. On each step we extract the smallest element num from heap and put 2*num to this heap if it is possible and update range. How we can understand if we need to put new element to heap? We need to keep pairs (num, limit) in our heap, for example:

3 -> candidates (3,6), what we put it heap on the first step is (3, 6).
12 -> candidates (3, 6, 12), what we put in heap on the first step is (3, 12).

Also we need to keep maximum value of elements in heap Max and update it when needed.

Complexity: time complexity is O(m log n), where n is length of nums and m is total number of candidates, we can estimate it as m = O(n log K), where K is the biggest number. Finally, it will be O(n log n log K). Space complexity is O(n) to keep our heap.
'''
class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        for num in nums:
            tmp = num
            while tmp%2 == 0: tmp//=2
            heap.append((tmp, max(num, tmp*2)))

        Max = max(i for i,j in heap)
        heapify(heap)
        ans = float("inf")

        while len(heap) == len(nums):
            num, limit = heappop(heap)
            ans = min(ans, Max - num)
            if num < limit:
                heappush(heap, (num*2, limit))
                Max = max(Max, num*2)

        return ans
def main():
    pass


if __name__ == "__main__":
    main()

