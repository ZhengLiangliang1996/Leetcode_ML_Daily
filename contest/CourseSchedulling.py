#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        import heapq
        courses.sort(key=lambda x:x[1])
        pq = []
        time = 0 
        for duration, end in courses:
            heapq.heappush(pq, -duration) # 最小堆， 返回最大的duration 
            time += duration
            # sum of the durations is less than lastDay then could take the course 
            # otherwise you can't 
            if time > end:
                time += heapq.heappop(pq)
        
        return len(pq)
