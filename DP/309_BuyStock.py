class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        if n == 0 or n == 1:
            return 0
        
        cool = [0] * n
        keep = [0] * n
        sold = [0] * n
        keep[0] = -prices[0]
        
        
        for i in range(1, n):
            sold[i] = keep[i - 1] + prices[i]
            cool[i] = max(cool[i - 1], sold[i-1])
            keep[i] = max(keep[i - 1], cool[i - 1] - prices[i])
            
        
        return max(sold[n-1],cool[n-1])
        
        
    
        
        