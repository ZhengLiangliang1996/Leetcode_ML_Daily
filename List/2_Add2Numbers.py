# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        def l2n(l1):
            res = 0
            count = 0
            while l1 != None:
                res += l1.val * (10 ** count)
                count += 1
                l1 = l1.next
            return res 
        
        res = l2n(l1) + l2n(l2)
        
        add = str(res)
        
        head = ListNode(add[len(add) - 1])
        answer = head
        
        for i in range(len(add)-2, -1, -1):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer
