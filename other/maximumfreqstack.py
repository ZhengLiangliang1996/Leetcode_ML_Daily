#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

class FreqStack:

    def __init__(self):
        self.counter = dict()
		#self.counter[number] = frequency of the number

        self.l = [[]]
		#self.l[frequency] = list of the numbers of the same frequencies,
		#youngest last. The first list in a list is a dummy (0 frequent)

        self.mfreq = self.lth = 0
		#maximum frequency and the length of self.l, respectively

    def push(self, x: int) -> None:
        if x not in self.counter:
            self.counter[x] = 1
        else:
            self.counter[x] += 1
        tmp = self.counter[x]
        if self.mfreq < tmp and self.lth < tmp:
            self.l.append([x])
            self.mfreq = self.lth = tmp
        elif self.mfreq < tmp:
            self.l[tmp].append(x)
            self.mfreq = tmp
        else:
            self.l[tmp].append(x)

    def pop(self) -> int:
        tmp = self.l[self.mfreq].pop()
        if self.l[self.mfreq] == []:
            self.mfreq -= 1
        self.counter[tmp] -= 1
        return tmp

def main():
    pass


if __name__ == "__main__":
    main()

