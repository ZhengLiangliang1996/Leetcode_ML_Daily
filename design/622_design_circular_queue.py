#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.length = k
        self.full = False
        self.queue = collections.deque()

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.popleft()
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[0]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[len(self.queue)-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.queue) == self.length:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
def main():
    pass


if __name__ == "__main__":
    main()

