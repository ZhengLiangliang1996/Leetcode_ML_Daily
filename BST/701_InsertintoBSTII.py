# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            node = TreeNode(val)
            return node
        if val < root.val:
            if not root.left:
                node = TreeNode(val)
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                node = TreeNode(val)
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        return root


# class Solution(object):
#     def insertIntoBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if not root:
#             return TreeNode(val)
#         if val > root.val:
#             root.right = self.insertIntoBST(root.right, val)
#         if val < root.val:
#             root.left = self.insertIntoBST(root.left, val)
#         return root

        
        
        
        