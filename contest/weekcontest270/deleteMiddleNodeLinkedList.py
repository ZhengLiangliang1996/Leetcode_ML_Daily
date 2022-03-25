#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return head 
        dummy = ListNode()
        dummy.next = head 
        if not head.next: 
            head = None 
        
        low, fast = dummy, dummy 
        while fast.next and fast.next.next:
            low = low.next 
            fast = fast.next.next 
        
        low.next = low.next.next
        return head 
        
            
