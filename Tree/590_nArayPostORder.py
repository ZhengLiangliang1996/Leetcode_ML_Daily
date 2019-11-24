"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        res = []
        
        for c in root.children:
            res.extend(self.postorder(c))
        res.append(root.val)
        
        return res
        