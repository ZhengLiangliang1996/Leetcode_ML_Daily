#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
  def letterCasePermutation(self, S):
    ans = []
 
    def dfs(S, i, n):
      if i == n:
        ans.append(''.join(S))
        return
      
      dfs(S, i + 1, n)      
      if not S[i].isalpha(): return      
      S[i] = chr(ord(S[i]) ^ (1<<5))
      dfs(S, i + 1, n)
      S[i] = chr(ord(S[i]) ^ (1<<5))
    
    dfs(list(S), 0, len(S))
    return ans


def main():
    s = Solution()
    a = s.letterCasePermutation('a1b2cU')
    print(a)


if __name__ == "__main__":
    main()

