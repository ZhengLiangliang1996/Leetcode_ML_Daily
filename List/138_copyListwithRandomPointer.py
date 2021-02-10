#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #based on the hint
        if not head:
            return head

        dummy = Node(0)
        dummy.next = head
        #interwived list !!!!插入一个之后curr要指向node.next而不是curr.next 连续错两次!
        curr = head
        while curr:
            node = Node(curr.val)
            node.next = curr.next
            curr.next = node
            curr = node.next

        # point to the right random
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        # take only the next
        pre, post = dummy, dummy.next
        while post:
            pre.next = post.next
            pre = post
            post = post.next


        return dummy.next


def main():
    pass


if __name__ == "__main__":
    main()

