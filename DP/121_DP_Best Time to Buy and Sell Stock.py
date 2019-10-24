class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态转移方程
        # maxProfit[i] = if prices[i-1] < prices[i]
        
        if not prices:
            return 0
        
        maxProfit = [0] * len(prices)
        lowest = [0] * len(prices)
        
        #初始化
        maxProfit[0] = 0
        lowest[0] = prices[0]
        
        for i in range(1, len(prices)):
            lowest[i] = min(lowest[i - 1], prices[i])
            maxProfit[i] = max(maxProfit[i - 1], prices[i] - lowest[i - 1])
            
        return max(maxProfit)
            