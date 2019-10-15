# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # need to compare parents and depth,
        # then store them together, using node.val as index 

        # if root is none
        if root == None:
            return False
        
        depth = 0
        
        # 可以保存相同的key 不同的value  k:('1','2')
        m = collections.defaultdict(tuple)
        
        # create queue
        
        q = [(root, None)]
        
        # BFS
        while q:
            sizeQ = len(q)
            for i in range(sizeQ):
                node, parent = q.pop(0)
                if not node:
                    continue
                
                # enqueue 
                m[node.val] = (parent, depth)
                q.append((node.left, node))
                q.append((node.right, node))
            depth += 1
        
        (xp, xd) = m[x]
        (yp, yd) = m[y]
        
        return xp != yp and xd == yd 