# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p == q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        #这里判断了结构的相同和值的相同
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        