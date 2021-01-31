#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #规律题目
        '''
        那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，然后再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：

    1　　[2]　　7　　4　　3　　1

    1　　[2]　　7　　4　　[3]　　1

    1　　[3]　　7　　4　　[2]　　1

    1　　3　　[1　　2　　4　　7]
        '''
        #逆向寻找,找到第一个nums[i] < nums[i+1]的值,
        #交换两个数,并且i后面的值全部反过来
        n = len(nums)
        #从后往前找
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j >=0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = nums[i+1:][::-1]
def main():
    pass


if __name__ == "__main__":
    main()

