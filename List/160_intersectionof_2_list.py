#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''
        The idea of solution is the following:

Calculate lengths of both lists and evaluate difference.
Make this number of steps for the longest list, pointer p1 and pointer p2 put to start of short list.
Move pointers p1 and p2 one by one until we have the same value: it will be either common element or it will be None element.
Suprasingly all this can be done in one loop: let us look at the line
currB = headA if currB is None else currB.next.
What we are doing here is when some list finishes we start to traverse another list. Imagine the case:

First list has a elements before intersection and b elements after intersection.
Second list has c elements before intersection and b elements after intersection, and c > a.

On the first step we will reach end of first list and for the second list we will be c-a elements before end.
On the second step our short list ended, so now we start to traverse long list and after c-a steps one of the pointers will be in the beginning of short list and another will be c-a steps from the long list.
Finally, we move both pointers with speed one and either we will have common element or they both reach the end in the same time and in this case they will have common None element.
Complexity: we traverse both lists twice, so we will make no more than 2n + 2m = O(m+n). Space complexity is O(1).
        '''
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB

        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
def main():
    pass


if __name__ == "__main__":
    main()

