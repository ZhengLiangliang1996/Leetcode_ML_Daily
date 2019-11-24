# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        leftH = self.height(root.left)
        rightH = self.height(root.right)
        return abs(leftH - rightH) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # tree height
    def height(self, root):
        if root == None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
            