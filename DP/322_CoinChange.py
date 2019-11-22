class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        invalid = 2 ** 32 
        dp = [invalid] * (amount + 1)
        
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[-1] == invalid else dp[-1]
    