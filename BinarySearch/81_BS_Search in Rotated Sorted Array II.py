class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            # 有重复值 所以需要让l 移动到不同的值
            while l < r and nums[l] == nums[r]:
                l += 1
                
            mid = l + ((r - l) >> 1)
            
            if nums[mid] == target:
                return True
            
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False