"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        res = []
        
        if root == None:
            return res
        
        q = []
        q.append(root)
        
        while q:
            res.append([node.val for node in q])
            
            new = []
            for node in q:
                for nodenode in node.children:
                    if nodenode != None:
                        new.append(nodenode)
            
            q = new
            
        return res