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

    def addTwoNumbersi_version1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return 0

        res = 0
        step = 0

        while True:
            if not l1 and not l2:
                break
            elif l1 and l2:
                res += (l1.val + l2.val) * (10 ** step)
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                res += (l1.val) * (10 ** step)
                l1 = l1.next
            elif not l1 and l2:
                res += (l2.val) * (10 ** step)
                l2 = l2.next

            step += 1

        # build up the list
        head = ListNode(-1)
        dummy = head
        while res >= 0:
            dummy.next = ListNode(res%10)     # 个位
            res /=10          # 取整
            if res == 0:
                break
            dummy = dummy.next

        return head.next

    def addTwoNumbersi_version1(self, l1, l2):
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
