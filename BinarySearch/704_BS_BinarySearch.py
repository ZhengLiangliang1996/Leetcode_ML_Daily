class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                r = mid 
            elif nums[mid] < target:
                l = mid + 1
        if l == len(nums): return -1 
        return l if nums[l] == target else -1
