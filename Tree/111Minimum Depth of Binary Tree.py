# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            # min depth tree is different from max depth tree
            # if one child is empty, then the depth should be the level of the other not 0 
            leftD = self.minDepth(root.left)
            rightD = self.minDepth(root.right)
            
            if leftD == 0 or rightD == 0:
                return leftD + rightD + 1
            else:
                return min(leftD, rightD) + 1
        