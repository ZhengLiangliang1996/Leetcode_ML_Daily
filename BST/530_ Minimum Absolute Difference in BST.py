# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        res = []
        def inorder(root):
            
            if root.left != None:
                inorder(root.left)
            if root != None and self.prev != None:
                res.append(abs(self.prev.val - root.val))
            self.prev = root
            if root.right != None:
                inorder(root.right)
        inorder(root)
        
        return min(res)