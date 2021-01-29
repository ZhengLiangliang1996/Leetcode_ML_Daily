# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 细节　两个坐标相同的时候　按照顺序进行输出

        # BFS
        res1 = []
        if not root:
            return res

        q = []
        q.append((root, 0, 0))

        while q:
            node, x, y = q.pop()
            # +y是因为后面sort的时候按照坐标排序
            res1.append((x, y, node.val))

            if node.left != None:
                q.append((node.left, x - 1, y + 1))
            if node.right != None:
                q.append((node.right, x + 1, y + 1))

        res1.sort()


        res2 = [[res1[0][2]]]
        for i in range(1, len(res1)):
            if res1[i][0] == res1[i - 1][0]:
                res2[-1].append(res1[i][2])
            else:
                res2.append([res1[i][2]])


        return res2

