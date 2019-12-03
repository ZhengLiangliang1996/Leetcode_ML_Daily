# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                #找出不顺序的第一个值了
                tmp = head.next
                q = dummy
                head.next = head.next.next
                
                while q.next and q.next.val <= tmp.val:
                    q = q.next
                    
                tmp.next = q.next
                q.next = tmp
        
        return dummy.next
        
        
        