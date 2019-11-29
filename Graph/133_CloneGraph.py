"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        q = []
        # node: original node
        if not node:
            return q
        
        hashtable = dict()
        
        # copied node
        copynode = Node(node.val, [])
        hashtable[node] = copynode
        
        
        q.append(node)
        while q:
            a = q.pop()
            
            if not a:
                continue
            
            for c in a.neighbors:
                if c not in hashtable:
                    hashtable[c] = Node(c.val, [])
                    q.append(c)
            
                hashtable[a].neighbors.append(hashtable[c])
        return copynode