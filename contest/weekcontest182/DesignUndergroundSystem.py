#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class UndergroundSystem:

    def __init__(self):
        self.record = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # station name
        t_in = t
        t_out = '#'
        if id in self.record:
            self.record[id].extend([stationName, '#', t, '#'])
        else:
            self.record[id] = [stationName, '#', t, '#']

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for i in range(len(self.record[id]) // 4):
            if id in self.record and self.record[id][3+4*i] == '#' and self.record[id][1+4*i] == '#':
                self.record[id][3+4*i] = t
                self.record[id][1+4*i] = stationName
                # print(self.record[id])
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg_sum, avg_num = 0.0, 0.0
        for k in self.record.keys():
            for i in range(len(self.record[k]) // 4):
                if self.record[k][0+4*i] == startStation and self.record[k][1+4*i] == endStation:
                    avg_sum += (self.record[k][3+4*i] - self.record[k][2+4*i])
                    avg_num += 1
        return float(avg_sum / avg_num)
    

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
