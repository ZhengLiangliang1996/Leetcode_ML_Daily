#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        n = len(times)
        arrival, leaving = [], []
        for i in range(n):
            arrival.append((times[i][0], i))
            leaving.append((times[i][1], i))
        arrival.sort()
        leaving.sort()
        available = list(range(n))
        seats = {}
        j = 0
        for t, p in arrival:
            while j < n and leaving[j][0] <= t:
                heappush(available, seats[leaving[j][1]])
                j += 1
            # 处理到达操作
            # 占据当前编号最小且未被占据的椅子
            seat = heappop(available)
            seats[p] = seat
            if p == targetFriend:
                # 如果当前人为目标，则返回对应的椅子
                return seat
        return -1
