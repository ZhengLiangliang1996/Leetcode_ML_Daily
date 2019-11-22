class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #dp[i][j]表示数据中前i个数字是否可以满足存在和为j的子数组
        
        nums.sort()
        
        if sum(nums) % 2 != 0:
            return False
        n = len(nums)
        target = sum(nums) / 2
        
        dp = [[False for i in range(target + 1)] for j in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]

                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
        
        return dp[-1][-1]
        
            
            