class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        n1 = len(s)
        n2 = len(p) 
        
        if n1 != 0 and n2 == 0:
            return False
        
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True
        
        for j in range(1, n2 + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if p[j - 1] != '*':
                    dp[i][j] = (p[j - 1] == '?' or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[-1][-1]
        