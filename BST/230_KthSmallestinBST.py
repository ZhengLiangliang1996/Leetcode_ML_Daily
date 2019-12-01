# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        class Solution {
public:
  int kthSmallest(TreeNode* root, int k) {
    return inorder(root, k);
  }
private:
  int inorder(TreeNode* root, int& k) {
    if (!root) return -1;
    int x = inorder(root->left, k);
    if (k == 0) return x;
    if (--k == 0) return root->val;
    return inorder(root->right, k);
  }
};
    
        def order(root, k):
            if not root:
                return -1
            x = inorder(root.left, k)
            if k == 0:
                return x
            if (k -= 1 == 0):
                return 
        
            
        
        