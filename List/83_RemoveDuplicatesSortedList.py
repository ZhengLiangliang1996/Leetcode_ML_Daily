#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        dummy = ListNode(0, head)


        while head and head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next





if __name__ == "__main__":
    main()

