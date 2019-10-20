class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        used = [0 for i in range(len(nums))]
        
        def dfs(curr):
            if len(curr) == len(nums) and curr not in res:
                res.append(curr)
                return 
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i - 1]:
                    continue
                if used[i]:
                    continue
                used[i] = 1
                dfs(curr+[nums[i]])
                used[i] = 0
        
        dfs([])

        return res