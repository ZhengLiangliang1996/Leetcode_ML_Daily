# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def sameTree(root1, root2):
            if root1 == root2 == None:
                return True
            
            if root1 == None or root2 == None:
                return False
            
            if root1.val != root2.val:
                return False
            
            return sameTree(root1.left, root2.right) and sameTree(root1.right, root2.left)
        
        return sameTree(root, root)
    
#     class Solution:
#   def isSymmetric(self, root):
#     def isMirror(root1, root2):
#       if not root1 and not root2: return True
#       if not root1 or not root2: return False
#       return root1.val == root2.val \
#         and isMirror(root1.left, root2.right) \
#         and isMirror(root2.left, root1.right)
#     return isMirror(root, root)/
    
    