# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n+1

        while l < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid) == True:
                r = mid 
            elif isBadVersion(mid) == False:
                l = mid + 1 
            elif isBadVersion(mid) == True:
                r = mid 
            
        return l
