# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.count = 0
        self.val_ = 0
        self.max_count = 0
        self.ans = []
        
        def visit(val):
            if self.count > 0 and val == self.val_:
                self.count += 1
            else:
                self.val_ = val
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.ans = []
                
            if self.count == self.max_count:
                self.ans.append(val)
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            visit(root.val)
            inorder(root.right)
            
        inorder(root)
        
        return self.ans