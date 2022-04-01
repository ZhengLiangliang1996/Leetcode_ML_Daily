#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Brute Force 
        # for i in range(n+1, 1224444+1):
        #     cnt = collections.Counter(str(i))
        #     if any(cnt[ch]!=int(ch) for ch in set(str(i))):
        #         continue
        #     if all(cnt[ch]==int(ch) for ch in set(str(i))):
        #         return i
        # return -1 
        # Pre calculation 
        
        
        # Permutation Algo + Binary Search 
        # Python function to print permutations of a given list
        L = []
        def perm(lst):
            if not lst: return []
            if len(lst) == 1: return [lst] 
            
            l = []
            for i in range(len(lst)):
                m = lst[i]
                remLst = lst[:i] + lst[i+1:]
                for p in perm(remLst):
                    if [m] + p not in l:
                        l.append([m] + p)
            return l
        L = ['1', '22', '333', '4444', '55555', '666666']
        possible = ['122', '1333', '14444', '22333', 
                    '122333', '155555', '224444', '1224444'];
        
        for psb in possible:
            for p in perm([char for char in psb]):
                L.append(''.join(p))
        L = [int(x) for x in L]
        L.sort()
        
        l,r = 0,len(L)
        while l<r:
            mid = l + (r - l) // 2
            if L[mid]<=n:           
                l = mid+1
            else:                       
                r = mid
        return L[l]
            
