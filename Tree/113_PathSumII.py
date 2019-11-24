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
        :rtype: List[List[int]]
        """
        
        
        res = []
        
        
        if not root:
            return res
        
        def dfs(root, s, path):
            if not root:
                return 
            
            if sum(path) == s and not root.left and not root.right:
                res.append(path)
                return 
            
            if root.left:
                dfs(root.left, s, path + [root.left.val])
            
            if root.right:
                dfs(root.right, s, path + [root.right.val])
        
        dfs(root, s, [root.val])
        
        return res
        
                
        

    