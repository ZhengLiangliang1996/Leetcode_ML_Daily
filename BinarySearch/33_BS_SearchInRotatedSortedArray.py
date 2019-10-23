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
            mid = l + ((r - l) >> 1)
            
            if nums[mid] == target:
                return mid
            
            #if nums[l] == target:
            #    return l
            
            #if nums[r] == target:
            #    return r
            
            # 找到左边递增 闭区间 [l,r],这样只需要nums[mid]来==，不然需要nums[l] == 和 nums[r] == 
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: #这里也能写满 nums[r] >= nums[mid]
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: bool
#         """
#         # 与33不同的是多了重复的元素
#         if not nums:
#             return False
        
#         left = 0
#         right = len(nums) - 1
        
#         while(left <= right):
#             # while left < right and nums[left] == nums[right]:
#             #     left += 1
            
#             mid = left + ((right - left) >> 1)
            
#             if nums[mid] == target or nums[left] == target or nums[right] == target:
#                 return True
            
#             if (target < nums[left] < nums[mid]) or (nums[mid] < target < nums[left]) or (nums[left] < nums[mid] < target):
#                 left = mid + 1
#             else:
#                 right = mid - 1
                
        
#         return False

def main():

    nums = [0,0,1,1,2,0]
    target = 2
    S = Solution()
    a = S.search(nums, target)
    print(a)
    # print(a)

if __name__ == "__main__":
    main()
                    
        
        