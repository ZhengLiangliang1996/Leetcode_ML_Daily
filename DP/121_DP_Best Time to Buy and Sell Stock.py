class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0 or 1] = ith day, bought[1] or sold or no stock[0], need to get dp[n-1][]
        if not prices: return 0 
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # -prices[i-1] comes from dp[i-1][0][0] - prices[i-1] max transaction= 0dp[...][0][0] is always 0 
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[n-1][0]
