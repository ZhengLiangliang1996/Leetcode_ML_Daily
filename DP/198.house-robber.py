#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rongcuo 
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
            
        total = [0] * len(nums)
        total[0] = nums[0]
        total[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            total[i] = max(total[i - 2] + nums[i], total[i - 1])

        return max(total)

# @lc code=end

