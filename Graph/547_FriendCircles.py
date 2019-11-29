class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if not M:
            return 0
        
        m = len(M)
        
        res = 0
        for i in range(m):
                if M[i][i] == 1:
                    res += 1
                    self.dfs(i, m, M)
        return res
    
    def dfs(self, curr, m, M):
        for i in range(m):
            if M[curr][i] == 1:
                M[curr][i] = M[i][curr] = 0
                self.dfs(i, m, M)
        