# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        if not root:
            return self.res
        
        def dfs(root, s):
            if not root.left and not root.right:
                self.res += s
                
            if root.left:
                dfs(root.left, s * 10 + root.left.val)
            if root.right:
                dfs(root.right, s * 10 + root.right.val)
                
        dfs(root, root.val)
        return self.res