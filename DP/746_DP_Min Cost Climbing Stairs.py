class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 记忆化递归
        df = [0 for i in range(len(cost) + 1)]
        
        def recur(n):
            # 走第一步和第0步 不需要cost
            if n <=1: 
                return 0
            
            if df[n] > 0:
                return df[n]
            
            df[n] = min(recur(n - 1) + cost[n - 1], recur(n - 2) + cost[n - 2])
            
            return df[n]
        
        return recur(len(cost))