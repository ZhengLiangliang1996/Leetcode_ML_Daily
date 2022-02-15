# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root: return res 
        def dfs(root, path):
            if not root.left and not root.right:
                res.append(path)
            
            if root.left:
                dfs(root.left, path + [str(root.left.val)])
            if root.right:
                dfs(root.right, path + [str(root.right.val)])
        
        dfs(root, [str(root.val)])
        
        res = ['->'.join(e) for e in res]
        return res 
