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
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        head1 = list1
        
        # find the start point 
        while a>1: 
            head1 = head1.next 
            a -= 1
        head2 = list1
        head3 = list2 
        while head3.next:
            head3 = head3.next 
        if a != b:
            while b>1:
                head2 = head2.next 
                b -= 1
            
        else:
            head2 = head1
        
        head3.next = head2.next.next 
        head1.next = list2 
        
        return list1
        
