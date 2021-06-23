#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head and not head.next:
            return head 
        gap = right - left 
        
        if gap == 0:
            return head 
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        for i in range(left-1):
            p = p.next
            
        c = p.next 
        n = c.next 

        for i in range(gap):
            tmp = n.next
            n.next = c
            c = n
            n = tmp
        
        p.next.next = n
        p.next = c
        
        return dummy.next 
        
        
                
            
