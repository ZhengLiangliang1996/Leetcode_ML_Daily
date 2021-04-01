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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ''' Solution 1:Space O(n), O(n)
        l=[]
        while head:
            l.append(head.val)
            head = head.next

        return l[::-1]  == l
        '''
        def reverse(h):
            curr = None
            nxt = h
            while nxt:
                tmp = nxt.next
                nxt.next =  curr
                curr=nxt
                nxt = tmp
            return curr

        # Step 1: go to the middle of the list
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # Step 2:  reverse the second half the list
        left,right = head, reverse(slow.next)
        # save for attaching it back(optional)
        save = right
        found = False
        while left and right:
            if left.val != right.val:
                found = True
                break
            left = left.next
            right = right.next
        slow.next = reverse(right)

        return not found





def main():
    pass


if __name__ == "__main__":
    main()

