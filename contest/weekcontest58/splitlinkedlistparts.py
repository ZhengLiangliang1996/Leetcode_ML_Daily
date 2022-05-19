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
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # check len of list 
        l = 0
        dummy = head
        while dummy:
            dummy = dummy.next 
            l += 1

        res = []
        p, r = l//k, l%k
        
        for i in range(k):
            dummy = ListNode(-1)
            dummy.next = head 
            if r > 0: 
                dummy = dummy.next
                r -= 1
            for j in range(p):
                dummy = dummy.next 
            res.append(head)
            head = dummy.next 
            dummy.next = None 

        return res 
