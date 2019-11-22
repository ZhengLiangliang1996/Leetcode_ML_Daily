class Solution(object):
    def maximalSquare(self, ma):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m = len(ma)
        n = len(ma[0])
        
        dp = [[0] * n for _ in range(m)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(ma[i][j])
                elif ma[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
                ans = max(ans, dp[i][j] * dp[i][j]) 
        
        
        return ans