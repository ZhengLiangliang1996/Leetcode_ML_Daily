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
        while l <= r:
            mid = l + ((r - l) >> 1)
            if(nums[mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        ansLow = l

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) >> 1)
            if(nums[mid] <= target):
                l = mid + 1
            else:
                r = mid - 1
        ansHigh = r

        return [ansLow, ansHigh] if ansLow <= ansHigh else [-1, -1]

    def searchRange_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target not in nums:
            return [-1, -1]

        def bisec_left(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        def bisec_right(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l


        return [bisect_left(nums, target), bisect_right(nums, target)-1]
def main():

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    S = Solution()
    a = S.searchRange(nums, target)
    print(a)
    # print(a)

if __name__ == "__main__":
    main()
