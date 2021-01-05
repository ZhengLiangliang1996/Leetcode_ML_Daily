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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0, head)

        pred = dummy

        while head:
            # if beginning of duplicates, skip all duplicates
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next
            else:
                pred = pred.next

            # move forward
            head = head.next

        return dummy.next


if __name__ == "__main__":
    main()

