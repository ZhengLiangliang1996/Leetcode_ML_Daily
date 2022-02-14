# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return self.res  
        
        def dfs(root):
            if not root: return 0 
            
            l = dfs(root.left)
            r = dfs(root.right)
            self.res = max(l+r, self.res)
            
            return max(l, r) + 1
        
        dfs(root)
        return self.res 
