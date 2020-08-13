# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = deque([(root, None)])

        while q:
            x_p, y_p = None, None
            for _ in range(len(q)):
                node, parent = q.popleft()
                if node.val == x:
                    x_p = parent
                elif node.val == y:
                    y_p = parent

                if x_p and y_p and x_p != y_p:
                    return True

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
        return False

