#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
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
        
        total = l2n(l1) + l2n(l2)

        # transfer 2 lists 
        # total = l2n(l1) + l2n(l2)
        addTwoNumbers = str(total)

        head = ListNode(add[len(add) - 1])
        answer = head
        
        for i in range(len(add)-2, -1, -1):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer
        
        # head = ListNode(total_string[len(total_string) - 1])
        # answer = head

        # for i in range(len(total_string) - 2, -1, -1):
        #     node = ListNode(total[i])
        #     head.next = node
        #     head = head.next
        
        # return answer

# @lc code=end

