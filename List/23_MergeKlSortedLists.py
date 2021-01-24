# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-1)
        move = head

        heap = []
        heapq.heapify(heap)

        [heapq.heappush(heap, (l.val, l)) for i, l in enumerate(lists) if l]
        while heap:
            curVal, curHead = heapq.heappop(heap)
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext

            if curHead:
                heapq.heappush(heap, (curHead.val, curHead))

        return head.next

    def newVersion(self, lists):
         #　i存在的意义就是当val相同时候
        # [1, 1, 2]  -> [4, 1, 2] -> [4, 3, 2] -> ....
        pairs = [(node.val, i, node) for i, node in enumerate(lists) if node]

        # 优先队列
        heapq.heapify(pairs)

        # create a new node
        dummy = ListNode(-1)
        head = dummy

        while pairs:
            val, i, node = heapq.heappop(pairs)
            head.next = node
            head = head.next

            if node.next:
                heapq.heappush(pairs, (node.next.val, i, node.next))

        return dummy.next


