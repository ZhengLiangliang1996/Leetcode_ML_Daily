class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findMin(nums, l, r):
            # only 2 elements 
            if l + 1 >= r:
                return min(nums[l], nums[r])
            
            # increasing sequence
            if nums[l] < nums[r]:
                return nums[l]
            
            mid = l + ((r - l) >> 1)
            
            return min(findMin(nums, l, mid - 1),
                       findMin(nums, mid, r))
        
        return findMin(nums, 0, len(nums) - 1)


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            while l < r and nums[r] == nums[l]:
                l += 1
            
            mid = l + ((r - l) >> 1 )
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        
        return nums[l]
            
