# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Solution1:dfs
#         def dfs(node, lower, upper):
#             if not node:
#                 return True
#             if lower is not None and node.val <= lower:
#                 return False
#             if upper is not None and node.val >= upper:
#                 return False
            
#             return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        
#         return dfs(root, None, None)
        
            
        # Solution: inorder traverse and check previous node
        # Do an in-order traversal, the numbers should be sorted, thus we only need to compare with the previous number.
        self.prev = None
        def inOrder(root):
            if root == None:
                return True
            if not inOrder(root.left):
                return False
            if self.prev != None and root.val <= self.prev.val:
                return False
            self.prev = root
            return inOrder(root.right)
        
        return inOrder(root)