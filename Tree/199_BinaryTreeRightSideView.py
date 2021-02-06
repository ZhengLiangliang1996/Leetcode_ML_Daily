#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        Like in many other problems about binary trees, we need to somehow traverse our tree, using dfs (inorder, preorder or postorder) or bfs. There are different solutions here, I use almost inorder traversal, with just one small change: instead of going Left -> Node -> Right, we will go Right -> Node -> Left. In this way we first visit nodes on the right side of our tree. Algorithm will look like this:

Create ans dictionary, which for each level H will keep the rightest node.
Traverse tree: first visit right children and if we do not have this H in ans yet, we put it there, then visit left children. Note again that with this order of traversal we always will put the rightest node for each level and next time we visit this level we will do nothing.
Finally, create list from our dictionary.
Complexity: time complexity is O(n) for classical dfs, space is O(h), again classical complexity for dfs as well as this amount of space we need to keep in our answer.

        ans = {}

        def dfs(root, H):
            if not root:
                return root

            dfs(root.right, H + 1)
            if H not in ans: ans[H] = root.val
            dfs(root.left, H + 1)

        dfs(root, 0)
        res = [ans[i] for i in range(len(ans))]
        return res
        '''
        if not root:
            return root

        # BFS
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            r = []
            qSize = len(q)
            for i in range(qSize):
                node = q.popleft()
                r.append(node.val)
                if node.right:
                    q.append(node.right)
                    r.append(node.right.val)
                if node.left:
                    q.append(node.left)
                    r.append(node.left.val)
            if len(r) >= 1:
                res.append(r[0])

        return res



def main():
    pass


if __name__ == "__main__":
    main()

