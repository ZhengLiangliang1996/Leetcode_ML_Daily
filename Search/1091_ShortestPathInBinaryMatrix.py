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
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        if grid[0][0] or grid[n-1][m-1]:
            return -1
        if n == 1 and m == 1 and grid[0][0] == 0:
            return 1

        d = [[0, 1], [0, -1], [-1, 0], [1, 0], [-1,-1], [1, 1], [-1, 1], [1, -1]]
        def bfs(x, y):
            visited = [[0 for i in range(m)] for j in range(n)]
            visited[x][y] = 1
            q = collections.deque()
            q.append((x, y))
            step = 1
            res = float('inf')
            while q:
                qSize = len(q)
                step += 1
                for i in range(qSize):
                    x1, y1 = q.popleft()

                    for j in range(8):
                        xx = x1 + d[j][0]
                        yy = y1 + d[j][1]

                        if xx < 0 or xx >= n or yy < 0 or yy >= m:
                            continue
                        if visited[xx][yy] == 1 or grid[xx][yy] == 1:
                            continue
                        if grid[xx][yy] == 0 and not visited[xx][yy] and xx == n-1 and yy == m-1:
                            res = min(res, step)
                        if grid[xx][yy] == 0:
                            q.append((xx, yy))
                        visited[xx][yy] = 1

            return res

        res = bfs(0, 0)

        return res if res != float('inf') else -1
if __name__ == "__main__":
    main()

