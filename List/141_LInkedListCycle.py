# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
#         if not head or not head.next:
#             return False
        
#         s = set()
#         tmp = head
        
#         while tmp:
#             if tmp in s:
#                 return True
            
#             s.add(tmp)
            
#             tmp = tmp.next
        
#         return False
         
        # Solution 2:
        slow = head
        fast = head
        while fast:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False