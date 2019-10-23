class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        
        while l < r:
            mid = l + ((r - l) >> 1)
            mid1 = mid + 1
            
            if A[mid1] > A[mid]:
                l = mid1
            else:
                r = mid
        return l