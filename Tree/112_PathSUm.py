# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #递归的第一步都是放手
        if not root:
            return False
        
        if not root.left and not root.right:
            return s == root.val
        
        return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)