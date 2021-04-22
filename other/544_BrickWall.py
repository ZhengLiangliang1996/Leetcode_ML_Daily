#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
'''
尽可能少的穿过砖块，也就是画一条线能经过更多的砖块之间的空隙（两头不算）。那么思路就转成了，我们要统计出所有的位置中，哪里的空隙出现的次数最多。

所以，我们从上到下遍历每层，从左到右遍历每个砖块的边缘，用hashmap保存每个边缘和左边界的距离以及该位置出现的次数。那么我们只要找出某个空隙的位置出现的次数最多就好。

由于是求穿过的砖块的个数，所以需要用砖块的行数减去孔隙数。
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/80526298
'''
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counter: Counter[int] = collections.Counter()
        for row in wall:
            width: int = 0
            for brick in row[:-1]:
                width += brick
                counter[width] += 1
        return len(wall) - max(counter.values(), default=0)
def main():
    pass


if __name__ == "__main__":
    main()

