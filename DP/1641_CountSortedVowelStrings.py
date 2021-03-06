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
我们想象n个球，包括第一个球之前、最后一个球之后，总共n+1个位置。如果任意选出四个位置插入四块板子，那么它们隔出了五个区间。这五个区间其实就对应着一种aeiou的序列：每个区间内球的个数，就代表了对应的字母的个数。举个例子。n=6时，在0,1,2,3,4,5,6里面抽取的是0,2,3,5，那么对应的插板方案就是

| O O| O| O O| O
对应的序列就是eeioou

所以上面的方案里，序列总数是组合数C(n+1,4)。

但是上面的方法有一个问题，那就是除了a和u可以是零个之外，其他的三个区间都至少有一个球。这并不合题意。解决的方案是，除了这n+1个位置，我们还添加三个选项：第1块板和第2块板重合，第2块板和第3块板重合，第3块板和第4块板重合。这样总共有n+4个候选项，依然是随机选择4个。我们发现，如果选到的四个都是隔板的位置，那么就和之前的方案一样。如果选到的是三个是隔板的位置，另外一个是某“重合”选项，我们发现这也能对应一种aeiou的序列。

举个例子。n = 6, 这样有10个候选：0,1,2,3,4,5,6,板12重合，板23重合，板34重合。如果抽到了是3,4,7,板23重合，那么对应的插板方案就是：

 O O O | O || O O |
对应的序列就是 aaaeoo

其他组合方式同理，无论从candiates里面如何抽取四个，都可以翻译为一种合理的插板方案，继而对应为一种合理的字母序列。

所以答案就是C(n+4,4).

很明显的DP问题。令dp[i][k]表示截止到第i个字符为止，第i个字符是字母k的方案数。根据题意，第i-1个字符必须小于等于k。

for (int j=0; j<=k; j++)
  dp[i][k] += dp[i-1][j];
返回的结果是 sum{dp[n-1][k]} k=0,1,2,3,4
'''
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        def help(n, m):
            cnt = 1
            for i in range(m):
                cnt *= n - i
                cnt /= i+1

            return cnt

        return help(n+4, n)


if __name__ == "__main__":
    main()

