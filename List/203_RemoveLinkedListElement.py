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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head 
        
        dummy = ListNode(-1)
        dummy.next = head 
        pre = dummy
        while head:
            print(pre.val)
            if head.val == val:
                pre.next = head.next 
                head = head.next
            else:
                head = head.next 
                pre = pre.next 
            
        return dummy.next 
        
