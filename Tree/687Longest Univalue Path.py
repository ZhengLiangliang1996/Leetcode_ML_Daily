# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.res = 0
        
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            pl = 0
            pr = 0
            if root.left and root.val == root.left.val:
                pl = l + 1
            if root.right and root.val == root.right.val:
                pr = r + 1
            self.res = max(self.res, pl + pr)
            
            return max(pl, pr)
        
        helper(root)
        return self.res
        