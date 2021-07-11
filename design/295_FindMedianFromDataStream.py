#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num):
        self.arr.add(num)

    def findMedian(self):
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n//2]
        return float((self.arr[n//2] + self.arr[n//2-1])) / 2
