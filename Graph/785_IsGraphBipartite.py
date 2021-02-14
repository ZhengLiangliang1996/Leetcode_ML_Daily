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
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        '''
        Here I do absolutely the same idea, but with a bit more clear coding style and also we do not need to create adjacency list here, it is already given in this way. The idea is the following: we traverse our graph and color our nodes int two colors 0 and 1: first one for nodes which can be reached with even number of steps and 1 for odd number of steps. Also we keep self.loop flag, which is true if we found odd loop, that is our graph is not bipartite.

        We define color array with -1 inside and then we start dfs from every node, and color our graph (note, that graph can have several connected components, so we need to start dfs from all nodes).
        '''
        def dfs(start):
            if self.conflict: return # early stop

            for neib in graph[start]:
                if color[neib] >= 0 and color[neib] == color[start]:
                    self.conflict = True
                elif color[neib] < 0:
                    color[neib]  = color[start]^1
                    dfs(neib)

        def bfs(start):
            q=collections.deque()
            q.append(start)
            while q:
                node = q.popleft()
                for neib in graph[node]:
                    if self.conflict:
                        return
                    if color[neib] >=0 and color[neib] == color[node]:
                        self.conflict = True
                    elif color[neib] < 0:
                        color[neib] = color[node]^1
                        q.append(neib)

            return

        n =  len(graph)
        self.conflict, color=  False, [-1]*n

        for i in range(n):
            if self.conflict: return False # stop if we  found  conflict
            if color[i] ==  -1:
                color[i] = 0
                bfs(i)

        return  True
def main():
    pass


if __name__ == "__main__":
    main()

