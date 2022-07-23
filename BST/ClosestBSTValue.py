#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

class Solution():
    def cloestValueBST_recursion(self, root, target, closest):
        if not root:
            return closest
        if abs(root.val - target) < abs(closest - target):
            closest = root.val 
        if root.val == target:
            return root.val
        elif root.val > target:
            return self.cloestValueBST_recursion(root.left, target, closest)
        else:
            return self.cloestValueBST_recursion(root.right, target, closest)

    def cloestValueBST_iteration(self, root, target, closest):
        currentNode = root

        while currentNode:
            if abs(currentNode.val - target) < abs(closest - target):
                closest = currentNode.val 
            if currentNode.val == target:
                return currentNode.val
            elif root.val > target:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return closest

def main():
    # TEST CASE 
    r = TreeNode(8)
    r.left = TreeNode(6)
    r.right = TreeNode(15)
    r.left.left = TreeNode(2)
    r.left.right = TreeNode(7)
    r.right.left = TreeNode(12)
    r.right.right = TreeNode(20)
    
    s = Solution()
    c1 = s.cloestValueBST_recursion(r, 18, float('inf'))
    c2 = s.cloestValueBST_iteration(r, 18, float('inf'))
    print(c1, c2)

if __name__ == '__main__':
    main()
