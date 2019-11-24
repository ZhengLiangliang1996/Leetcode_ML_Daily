# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #重点！　相同的边不能被访问两次　所以在使用递归的时候返回的只能是左右中最大的那边的sum
        
        self.res = float('-inf')
        
        def maxPathHelp(root):
            if not root:
                return 0
            
            l = max(0, maxPathHelp(root.left))
            r = max(0, maxPathHelp(root.right))
            
            #当前这一层已经访问过
            self.res = max(l + r + root.val, self.res)
            #返回的时候只能返回一边在递归时候
            return max(l, r) + root.val
        
        maxPathHelp(root)
        
        return self.res