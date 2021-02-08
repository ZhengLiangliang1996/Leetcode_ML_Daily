#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
'''
This is more design problem, not algorithmic one in my opinion. You already given implemented class iterator, which you can understand as list, but it is not list. The goal is to implement so-called peeking iterator and to do this we need to be one step ahead: let us create self.buffer variable, which will keep next value from our iterator.

When we call peek function, we just return value from our buffer.
When we call next function, we write buffer variable to tmp, then we update our buffer: if we have next element, we go to the next element, if we do not have it we make it equal to None.
Finally, hasNext function now is just checking if buffer is empty or not.
Complexity: it is O(1) for all operations, if it was O(1) for original iterator class.
'''
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        # create self.buffer variable, which will keep next value from our iterator.
        self.buffer = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer


    def next(self):
        """
        :rtype: int
        """
        tmp = self.buffer
        self.buffer = self.buffer = self.iter.next() if self.iter.hasNext() else None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer != None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
def main():
    pass


if __name__ == "__main__":
    main()

