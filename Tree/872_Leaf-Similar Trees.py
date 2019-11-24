# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        
        def preOrder(root, res):
            if root != None:
                if root.left == None and root.right == None:
                    res.append(root.val)
                else:
                    if root.left != None:
                        preOrder(root.left, res)
                    if root.right != None:
                        preOrder(root.right, res)
            
        preOrder(root1, res1)
        preOrder(root2, res2)
        
        if len(res1) != len(res2):
            return False
        else:
            for i in range(len(res1)):
                if res1[i] != res2[i]:
                    return False
                
        return True
        # return res1 == res2
    
            