class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        def dp1(n1, n2):
            if n1 == 0:
                return n2
            
            if n2 == 0:
                return n1
            
            if dp[n1][n2] > 0:
                return dp[n1][n2]
            
            if word1[n1 - 1] == word2[n2 - 1]:
                dp[n1][n2] = dp1(n1 - 1, n2 - 1)
            else:
                dp[n1][n2] = min(dp1(n1 - 1, n2), 
                                 dp1(n1, n2 - 1),
                                 dp1(n1 - 1, n2 - 1)) + 1
            return dp[n1][n2]
        
        return dp1(n1, n2)
            
            
