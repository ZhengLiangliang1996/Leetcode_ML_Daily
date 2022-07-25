#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution():
    # T: O(N^2), S: O(1)
    def sort_stack(self, stack):
        if not stack:
            return stack 
        top = stack.pop()
        self.sort_stack(stack)
        self.insert_stack(stack, top)
        return stack

    def insert_stack(self, stack, element):
        if not stack or element >= stack[-1]:
            stack.append(element)
            return 
        # if element is less than the stack top, pop first and insert and then append 
        top = stack.pop()
        self.insert_stack(stack, element)
        stack.append(top)
    # T: O(N^2), S: O(N)
    def sort_stack1(self, stack):
        # using external space
        t = []
        while stack:
            top = stack.pop()
            if t and t[-1] < top: stack.append(t.pop())
            t.append(top)
        # t now is the reverse sorted stack, pop it back to stack
        while t:
            stack.append(t.pop())

        return t 

s = Solution()
print(s.sort_stack([1, 3, 4, -2, 2, 5]))
print(s.sort_stack1([1, 3, 4, -2, 2, 5]))
