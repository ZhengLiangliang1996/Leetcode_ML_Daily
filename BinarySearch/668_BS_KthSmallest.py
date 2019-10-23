class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        
        l = 1 
        r = m * n + 1
        
        def lex(x, m, n):
            count = 0
            for i in range(1,m+1):
                count += min(n, x / i)
            
            return count
        
        while l < r:
            mid = l + ((r - l) >> 1)
            
            # 找到第k个 大于或者等于k个的时候
            if lex(mid, m, n) >= k:
                r = mid
            else:
                l = mid + 1
        
        return r # 返回l和r都一样