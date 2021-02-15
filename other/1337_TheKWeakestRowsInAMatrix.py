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
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        '''
        Buckets solution
This problem is marked as easy on leetcode, because dimensions of problem is quite small and given solution will be fast enough. However we did not use some information given in problem statement, so we can improve our performance:

First of all, in each row data is sorted, like [1, 1, 1, ..., 0, 0, 0], and we do not really need to traverse all list to find how many ones we have inside, and we can do binary search instead with complexity O(log n), so complexity of first step will be O(m log n) instead of O(mn). Unfortunatelly you can not use bisect library here, because data in rows sorted in reverse order and you need to do it by hands.
Secondly, we do not need to sort all data, but we only need to choose k smallest elements, which can be done, using heaps: we can keep heap with k elements and have complexity O(m log k). Moreover, because frequencies will not be more than n, we can use bucket sort to find k smallest values.
Final time complexity will be O(m log n + n), space complexity is O(n). If m log k << n, it is more preferable to use heaps, however even though complexity of heap operations is O(log k), constant is quite big, so I can say, bucket sort is preferable.

class Solution:
    def kWeakestRows(self, mat, k):
        def num_ones(L):
            beg, end = 0, n
            while beg < end:
                mid = (beg + end)//2
                if L[mid] > 0:
                    beg = mid + 1
                else:
                    end = mid
            return beg

        m, n = len(mat), len(mat[0])
        buckets = [[] for _ in range(n+1)]
        for i, row in enumerate(mat):
            buckets[num_ones(row)].append(i)

        return list(chain(*buckets))[:k]
        '''

#         n=len(mat)
#         m=len(mat[0])
#         if n == 1 and m == 1 and k == 1:
#             return  [0]

#         sodCount = []
#         for idx, ele in enumerate(mat):
#             sodCount.append((sum(ele), idx))

#         sodCount.sort()

#         res = []
#         for i in range(k):
#             res.append(sodCount[i][1])
#         return  res
#         改成一行
#         Complexity: time complexity is O(mn) to evaluate all sums and O(m*log m) to perform sort and choose k smallest elements, so final complexity is O(mn + m log m). Space complexity is O(m).
        return [j for _, j in sorted([(row, idx) for idx, row in enumerate(mat)])][:k]

def main():
    pass


if __name__ == "__main__":
    main()

