class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        DP solution:
        M[i][j] denotes if s[0,..,i-1] matches p[0,..,j-1]
        Then the recurisve function of M[i][j] is:
        1. If p[j-1] is a character other than "*" and ".":
            M[i][j] = M[i-1][j-1] && s[i-1] == p[j-1]
        2. If p[j-1] is ".":
            M[i][j] = M[i-1][j-1]
        3. If p[j-1] is "*":
            1) If "*" matches 0 p[j-2]:
                M[i][j] = M[i][j-2]
            2) If "*" matches 1 p[j-2]:
                M[i][j] = M[i][j-1]
            3) If "*" matches multiple p[j-2], M[i][j] is true iff:
                a. s[i-1] == p[j-2] or p[j-2] is ".", and
                b. M[i-1][j] is true
        """
        
        
        n1 = len(s)
        n2 = len(p)
        
        if n1 != 0 and n2 == 0:
            return False
        
        dp = [[False for _ in range(n2+1)] for _ in range(n1 + 1)]
        dp[0][0] = True
        
        for j in range(2, n2+1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if p[j - 1] != '*':
                    dp[i][j] = (p[j - 1] == '.' or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or ((p[j - 2] == '.' or p[j - 2] == s[i - 1]) and dp[i-1][j])
        
        return dp[-1][-1]