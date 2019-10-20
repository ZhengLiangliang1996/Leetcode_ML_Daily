class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(nums) - 1
        res = []
        # find first position 
        # 
        while(l < r):
            mid = l + ((r - l) >> 1) 
            print(l)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
            
        if l == len(nums) or nums[l] != target:
            res.append(-1)
        else: 
            res.append(l)
        
        l = 0
        r = len(nums) - 1
        print('-----')
        
        while(l < r):
            mid = l + ((r - l) >> 1) 
            print(l)
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        l -= 1
        print('------')
            
        if l < 0 or nums[l] != target:
            res.append(-1)
        else:
            res.append(l)
        
        return res


def main():

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    S = Solution()
    a = S.searchRange(nums, target)
    print(a)
    # print(a)

if __name__ == "__main__":
    main()
