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
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        res = [-1, -1]
        
        tn = []
        pre = head
        nxt = head.next 
        cnt, minD, maxD = 0, float('inf'), 0
        while nxt.next:
            if (pre.val > nxt.val and nxt.val < nxt.next.val) or (pre.val < nxt.val and nxt.val > nxt.next.val):
                if tn: 
                    minD = min(minD, cnt - tn[-1])
                    maxD = max(maxD, cnt - tn[0])
                tn.append(cnt)
                
            nxt = nxt.next 
            pre = pre.next
            cnt += 1

        return res if maxD == 0 else [minD, maxD]
        
