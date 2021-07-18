#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    suc = None
    
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         count = self.getCount(head)
#         print(count)
#         newHead = head
#         for i in range(1,count+1,k):
#             if i+k-1 <= count:
#                 newHead = self.reverseBetween(newHead,i,i+k-1)
#         return newHead
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head is None or k == 1):
            return head 
        
        # First, get the length of the list
        length = self.getCount(head)
        
        # Second pass, swap in groups.
        newH = head 
        for i in range(1, length+1, k):
            if i+k-1 <= length:
                newH = self.reverseBetween(newH, i, i+k-1)
        
        return newH
    
    def getCount(self,node):
        n = node
        count = 0
        while n:
            count+=1
            n = n.next
        return count
    
    def reverseN(self,head, n):
        global suc 
        if n == 1:
            suc = head.next
            return head
        
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = suc
        return last
    
    def reverseBetween(self,head, m, n):
        if m == 1:
            return self.reverseN(head, n)
        
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        
        return head
