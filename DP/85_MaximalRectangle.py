class Solution(object):
    def maximalRectangle(self, ma):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not ma:
            return 0
        
        m = len(ma)
        n = len(ma[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        maxArea = 0
        
        
        
        for i in range(m):
            for j in range(n):
                if ma[i][j] == '1':
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1 
                else:
                    dp[i][j] == 0
                    
                minWidth = dp[i][j]
                for k in range(i, -1, -1):
                    height = i - k + 1

                    minWidth = min(minWidth, dp[k][j])

                    maxArea = max(maxArea, height*minWidth)
        
        return maxArea
    
    