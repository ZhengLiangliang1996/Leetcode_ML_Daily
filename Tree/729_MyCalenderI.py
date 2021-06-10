#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Node(object):
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar(object):
    '''
    当第一次调用book的时候，初始化root节点。之后再book的时候，根据start,end判断是否和当前节点的时间段有交叉，如果有交叉就返回False；如果没有交叉，那么就一直向下寻找到叶子节点，到了叶子节点仍然没有交叉的话，就新建节点。
    '''
    def __init__(self):
        self.root = None

    def book_helper(self, s, e, node):
        if node.e <= s:
            if node.right:
                return self.book_helper(s, e, node.right)
            else:
                node.right = Node(s, e)
                return True
        elif node.s >= e:
            if node.left:
                return self.book_helper(s, e, node.left)
            else:
                node.left = Node(s, e)
                return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.book_helper(start, end, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
