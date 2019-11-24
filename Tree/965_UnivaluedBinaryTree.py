# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.right and root.right.val != root.val:
            return False
        if root.left and root.left.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)