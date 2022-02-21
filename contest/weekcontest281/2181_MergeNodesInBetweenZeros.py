#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # adding up
        dummy = head 
        
        while head:
            if head.val == 0 and head.next:
                head = head.next 
            # adding up the following 
            else:
                first = head 
                head = head.next 
                while head and head.val != 0:
                    first.val += head.val
                    head = head.next 
                
                first.next = head
                
                
        head = dummy
        while head:
            if head.next and head.next.val == 0:
                head.next = head.next.next
            head = head.next

        return dummy.next 
