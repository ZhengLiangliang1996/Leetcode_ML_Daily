from bisect import bisect_right
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        
        l, r = matrix[0][0], matrix[-1][-1]+1
        
        while l < r:
            mid = l + ((r - l) >> 1)
            
            loc = sum(bisect_right(m, mid) for m in matrix)
            
            if loc == k:
                r = mid
            elif loc > k:
                r = mid 
            else:
                l = mid + 1
        
        return r