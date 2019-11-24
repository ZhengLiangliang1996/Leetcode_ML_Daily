# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #两层循环
        if not root:
            return 0
        
        return self.pathsumCount(root, s) + self.pathSum(root.left, s) +  self.pathSum(root.right, s) 
        
    def pathsumCount(self, root, s):
        res = 0
        
        if not root:
            return 0
        
        if root.val == s:
            res += 1
        
        res += self.pathsumCount(root.left, s - root.val)
        res += self.pathsumCount(root.right, s - root.val)
        return res