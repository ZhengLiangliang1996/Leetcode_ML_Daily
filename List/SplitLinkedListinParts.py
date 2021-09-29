#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air.localdomain>
#
# Distributed under terms of the MIT license.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        N = 0
        while cur:
            cur = cur.next
            N += 1
        d, r = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(d + (i < r) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
