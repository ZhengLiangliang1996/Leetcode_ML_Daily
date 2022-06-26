#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class subarraysum_prefix:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # special case 当前n个就是和是6的时候，sum1 存储的是0:-1
        # key: presum, value: index
        #
        d = {0:-1}
        prefix = nums[::]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i-1]
        # 核心思想 (sum1 + sum2) % k == 0
        # so sum1 % k == sum2 % k 
        # sum1 = 23 sum2 = 23+2+4
        for i, n in enumerate(prefix):
            r = n % k
            if r in d:
                if abs(i - d[r]) >= 2:
                    return True
            else:
                d[r] = i
        return False

class twosum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for idx, n in enumerate(nums):
            if (target - n) in d.keys():
                return [d[target - n], idx]
            else:
                d[n] = idx
