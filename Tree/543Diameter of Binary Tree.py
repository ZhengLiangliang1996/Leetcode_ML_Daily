# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.longest = float('-inf')
        
        def helper(root):
            if not root:
                return -1
            
            l = helper(root.left) + 1
            r = helper(root.right) + 1
            
            self.longest = max(l + r, self.longest)
            
            return max(l, r)
            
        helper(root)
        return self.longest