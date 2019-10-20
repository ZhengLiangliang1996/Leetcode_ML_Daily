class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0:
            return 0
        
        while(left <= right):
            mid = left + ((right - left) >> 1)            
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
                
        return right+1