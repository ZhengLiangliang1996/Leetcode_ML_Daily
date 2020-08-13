"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
import collections

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    q = collections.deque()
    if endWord not in wordList:
        return 0
    visited = set(wordList)
    q.append(beginWord)

    step = 0
    while q:
        qSize = len(q)
        step += 1
        for i in range(qSize):
            node = q.popleft()
            for j in range(len(node)):
                for k in 'abcdefghijklmnopqrstuvwxyz':
                    new = node[:j] + k + node[j+1:]

                    if new == endWord:
                        return step + 1
                    if new not in visited:
                        continue
                    if new in visited and new != node:
                        q.append(new)
                        visited.remove(new)

    return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    a = ladderLength(beginWord, endWord, wordList)
    print(a)
if __name__ == "__main__":
    main()

