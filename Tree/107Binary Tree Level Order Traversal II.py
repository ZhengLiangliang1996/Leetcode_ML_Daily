# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return []
        
        q = []
        q.append(root)
        
        while(q):
            res.append([node.val for node in q])
            
            new = []
            
            for node in q:
                if node.left != None:
                    new.append(node.left)
            
                if node.right != None:
                    new.append(node.right)
                
            q = new
        
        res.reverse()
        return res
        