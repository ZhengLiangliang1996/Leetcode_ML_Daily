# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if not root:
                res.append('#')
            else:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = deque(data.split(' '))
        def build(data):
            v = data.popleft()
            if v == '#':  
                return None
            node = TreeNode(int(v))
            node.left = build(data)
            node.right = build(data)
            return node
        return build(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
