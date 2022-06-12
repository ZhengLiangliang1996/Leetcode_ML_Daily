#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def numTeams(self, rating: List[int]) -> int:
    # 
    #出现在位置 jj 左侧且比 jj 评分低的士兵数量 i_less
    #出现在位置 jj 左侧且比 jj 评分高的士兵数量 i_more
    # j 右侧 评分低 k_less 
    # j 右侧 评分高 k_more 
 
        n = len(rating)
        ans = 0
        # 枚举三元组中的 j
        for j in range(1, n - 1):
            iless = imore = kless = kmore = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    iless += 1
                # 注意这里不能直接写成 else
                # 因为可能有评分相同的情况
                elif rating[i] > rating[j]:
                    imore += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    kless += 1
                elif rating[k] > rating[j]:
                    kmore += 1
            ans += iless * kmore + imore * kless
        return ans

        # LTE
#         self.res = 0
#         #@lru_cache()
#         def dfs(path, st):
#             if len(path) == 3:
#                 #if (path[0] > path[1] and path[1] > path[2]) or (path[0] < path[1] and path[1] < path[2]):
#                 self.res += 1
#                 return 
            
#             for i in range(st, len(r)):
#                 # pruning 
#                 if len(path) == 2 and path[0] > path[1]:
#                     if path[1] < r[i]:
#                         continue 
#                 elif len(path) == 2 and path[0] < path[1]:
#                     if path[1] > r[i]:
#                         continue
#                 if len(path) == 3:
#                     continue 
#                 dfs(path+[r[i]], i+1)
                
#         dfs([], 0)
#         return self.res 
