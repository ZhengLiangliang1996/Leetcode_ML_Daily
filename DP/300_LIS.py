class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0 or n == 1:
            return n

        LIS = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[j] + 1, LIS[i])

        return max(LIS) + 1


