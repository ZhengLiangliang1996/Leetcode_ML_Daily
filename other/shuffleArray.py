#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.num

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        cp = [x for x in self.num]
        random.shuffle(cp)
        return cp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
