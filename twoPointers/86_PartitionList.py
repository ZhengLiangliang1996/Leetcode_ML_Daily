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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        '''
         e.g, [1,4,3,2,5,2]
         d1->1->2->2
                   p1
         d2->4->3->5
                   p2

         connect p1->d2.next
         return d1.next

        '''
        l1 = ListNode(-1)
        l2 = ListNode(-1)

        p1, p2 = l1, l2

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = l2.next
        p2.next = None
        return l1.next

def main():
    pass


if __name__ == "__main__":
    main()

