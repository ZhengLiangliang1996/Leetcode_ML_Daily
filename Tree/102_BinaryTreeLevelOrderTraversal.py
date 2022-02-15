# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        q = collections.deque()
        q.append(root)
        
        while q: 
            Q = collections.deque()
            res.append([node.val for node in q])
            
            while q:
                node = q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            q = Q
            
    
        return res 
