class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # rongcuo 
        if not nums:
            return 0
        
        if n == 1 or n == 2:
            return max(nums)
        
        num1 = nums[1:]
        num2 = nums[:-1]
        
        total1 = [0] * (n - 1)
        total2 = [0] * (n - 1)
        
        total1[0] = num1[0]
        total2[0] = num2[0]
        total1[1] = max(num1[0], num1[1])
        total2[1] = max(num1[0], num2[1])
        
        if len(num1) == 2:
            return max(max(total1), max(total2))
        
        for i in range(1, n - 1):
            total1[i] = max(total1[i - 2] + num1[i], total1[i - 1])
            total2[i] = max(total2[i - 2] + num2[i], total2[i - 1])
        
        return max(max(total1), max(total2))
        
        
        