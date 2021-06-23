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
        
        
                
            # Here is an exmple
        # 1 --> 2 --> 3 --> 4 --> 5
        #       
        # Before first while-loop
        #      0 --> 1 --> 2 --> 3 --> 4 --> 5
        #      prev  curr
        # After first while-loop 
        #      0 --> 1 --> 2 --> 3 --> 4 --> 5 
        #            prev curr 
        #  last_unswapped, first_swapped = prev, curr
        # The following is the details for 2nd while-loop
        # diff=2 #   1 <-- 2 --> 3 --> 4 --> 5
        #                 prev  curr
        # diff=1 #   1 <-- 2 <-- 3 --> 4 --> 5
        #                       prev  curr
        # diff=0 #   1 <-- 2 <-- 3 <-- 4 --> 5
        #                             prev  curr
        # last_unswapped.next = prev
        # first_swapped.next  = curr
        # After impletenting the above two lines, we get:
        #         first_swapped.next = curr
        #          __________________  
        #          ^                 |      
        #          |                 V 
        # 1        2 <-- 3 <-- 4     5
        # |                    ^
        # V ___________________| 
        # last_unswapped.next=prev    
