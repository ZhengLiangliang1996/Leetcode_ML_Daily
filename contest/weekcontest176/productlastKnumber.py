#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import math

class ProductOfNumbers:
    def __init__(self):
        self.data = []

    def add(self, num: int) -> None:
        self.data.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.data[-k:])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
