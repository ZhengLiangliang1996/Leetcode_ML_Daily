class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        
        
        num1 = [0] * (max(nums)+1)
        
        for i in nums:
            num1[i] += i
        
        f = [0] * (max(nums) + 1)
        f[0] = num1[0]
        f[1] = max(num1[0], num1[1])
        
        for i in range(2, len(f)):
            f[i] = max(f[i - 1], f[i - 2] + num1[i])
        
        return max(f)
        
        