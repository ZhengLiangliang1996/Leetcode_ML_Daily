"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = collections.deque()

        stack.append(root)

        while stack:
            node = stack.pop()
            res.append(node.val)

            stack.extend(node.children[::-1])
        
        return res 
        

        
