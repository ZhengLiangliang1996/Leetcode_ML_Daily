"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head 
        
        q = []
        hashtable = dict()
        
        copynode = Node(head.val, head.next, head.random)
        
        hashtable[head] = copynode
        
        q.append(head)
        
        while q:
            a = q.pop()
            if not a:
                continue
            
            c = a.next
            d = a.random
            if c:
                if c not in hashtable:
                    hashtable[c] = Node(c.val, c.next, c.random)
                    q.append(c)
                hashtable[a].next = hashtable[c]
            
            if d:
                if d not in hashtable:
                    hashtable[d] = Node(d.val, d.next, d.random)
                    q.append(d)
                hashtable[a].random = hashtable[d]
            
        
        return copynode
        
            
                