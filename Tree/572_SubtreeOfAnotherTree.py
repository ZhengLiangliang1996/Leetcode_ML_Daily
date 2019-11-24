# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        if s == None:
            return False
        if(self.sameTree(s, t)):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
        
    
    def sameTree(self, root1, root2):
        if root1 == root2 == None:
            return True
        
        if root2 == None or root1 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        