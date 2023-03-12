# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1) 
        pre = res 
        if not list1 and not list2:
            return list1
        
        if list1 and not list2: return list1
        if not list1 and list2: return list2

        while list1 and list2: 
            if list1.val < list2.val:
                res.next = list1
                res = res.next 
                list1 = list1.next
            else:
                res.next = list2
                res = res.next 
                list2 = list2.next

        if list2: 
            res.next = list2 
        
        if list1:
            res.next = list1
        
        return pre.next 

        
