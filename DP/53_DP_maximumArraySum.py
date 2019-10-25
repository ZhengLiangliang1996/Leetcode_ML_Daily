class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = [0] * len(nums)
        
        maxSub[0] = nums[0]
        
        # 公式理解　若前一个数是负数，则不加入
        # maxSub[i] = maxSub[i - 1] > 0 ? maxSub[i - 1] + nums[i] : nums[i]
        for i in range(1, len(nums)):
            maxSub[i] = max(maxSub[i - 1] + nums[i], nums[i])
        
        return max(maxSub)