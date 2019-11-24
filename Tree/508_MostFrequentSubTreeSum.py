# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        if not root:
            return res
        
        def traverse(root):
            if not root:
                return 0
            s = traverse(root.left) + traverse(root.right) + root.val
            res.append(s)
            return s
        
        traverse(root)
        
        count = collections.Counter(res)
        f = max(count.values())
        
        return [x for x,v in count.items() if v == f]
            