class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0:
            return -1
        
        while left <= right:
            mid = left + ((right - left) >> 1)
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1 
            else:
                right = mid - 1
        
        return -1
        