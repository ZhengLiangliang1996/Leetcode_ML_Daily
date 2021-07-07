from bisect import bisect_right
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            mid = l + (r - l) // 2
            cnt = sum([bisect_right(n, mid) for n in matrix])

            if cnt >=k:
                r = mid
            else:
                l = mid + 1

        return l



