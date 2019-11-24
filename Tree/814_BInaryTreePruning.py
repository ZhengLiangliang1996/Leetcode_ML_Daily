# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 相当于post traverse 
        # # 
        # 一定要注意的是，我们判断这个节点是叶子节点并且节点值是1的这个步骤要放在左右子树处理之后。可以从Example2中看出来，如果0节点的左右子节点都是0，那么把左右节点都减去了之后，还要判断自身是不是0，然后把自己也剪了。也就是说这一步相当于后序遍历，把孩子都处理结束之后，然后再处理自身。
        
        if not root:
            return root
        if root.left != None:
            root.left = self.pruneTree(root.left)
        if root.right != None:
            root.right = self.pruneTree(root.right)
        return root if root.val == 1 or root.left or root.right else None
    