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
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        '''
        假设minimum effort是a，那么意味着路径上不能有超过diff大于a的边。怎么验证有没有呢？BFS走一遍就行。从左上角向外扩展，遇到diff大于a的边就绕行，看看最终能否到达右下角。成功的话，就尝试减小a；不成功的话，就尝试增大a。这个时间复杂度是o(M*N*logH)，H是矩阵元素的最大值。
        '''
        m = len(heights)
        n = len(heights[0])
        d = [[0,1],[0,-1],[-1,0],[1,0]]

        # BFS
        def isOK_BFS(heights, a):
            visited = [[0 for i in range(n)] for j in range(m)]
            visited[0][0] = 1

            q = collections.deque()
            q.append((0, 0))

            while q:
                x, y = q.popleft()
                for k in range(4):
                    i = x + d[k][0]
                    j = y + d[k][1]
                    if i < 0 or i >= m or j < 0 or j >=n:
                        continue
                    if visited[i][j] == 1:
                        continue
                    if abs(heights[i][j] - heights[x][y]) > a:
                        continue

                    q.append((i, j))
                    visited[i][j] = 1

            return visited[m-1][n-1] == True

        # Binary Search
        l = 0
        r = 1000000

        while l < r:
            mid = l + (r - l) // 2
            if (isOK_BFS(heights, mid)):
                r = mid
            else:
                l = mid + 1

        return l




def main():
    pass


if __name__ == "__main__":
    main()

