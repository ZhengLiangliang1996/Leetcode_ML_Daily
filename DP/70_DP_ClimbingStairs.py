class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 运用记忆化递归
        df = [0 for i in range(n+1)]
        def dpStairs(n):
            if n <= 1:
                return 1
            #记录下当前的值
            if df[n] > 0: return df[n]
            
            df[n] = dpStairs(n - 1) + dpStairs(n - 2)
            
            return df[n]
        
        return dpStairs(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1 
        fn_1, fn_2 = 1, 1
        for i in range(n-1):
            temp = fn_2
            fn_2 = fn_1 + fn_2
            fn_1 = temp
        
        return fn_2
