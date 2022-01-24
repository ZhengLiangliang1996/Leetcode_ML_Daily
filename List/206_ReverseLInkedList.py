# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         p = None 
#         c = head 
#         n = None 
#         while c:
#             # 定义
#             n = c.next 
#             # 反转 
#             c.next = p
#             # 下一步 
#             p = c 
#             c = n
        
#         return p

        if not head or not head.next:
            return head 
        
        last = self.reverseList(head.next)
        
        head.next.next = head 
        head.next = None 
        
        return last
                    
