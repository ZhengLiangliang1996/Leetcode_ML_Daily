#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

# Python program to find the inorder successor in a BST

# A binary tree node
class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inOrderSuccessor(n):
    # if right child exists
    if n.right:
        return findMin(n.right)
    else:
        # go up to find root 
        p = n.parent
        while p:
            if n != p.right:
                break
            n = p
            p = p.parent
        return p


def findMin(n):
    # recursively gose left to find min
    temp = n
    if temp.left:
        while temp.left:
            temp = temp.left
    return temp 


def insert(node, data):

    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:
        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


# Driver program to test above function

root = None

# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)
temp = root.left.right

succ = inOrderSuccessor(temp)

print(succ.data)
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

