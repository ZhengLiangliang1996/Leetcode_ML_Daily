class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    c = [0]
                    self.dfs(i, j, m, n, grid, c)
                    res = max(c[0], res)
        return res
    
    def dfs(self, x, y, m, n, M, c):
        if x < 0 or x >= m or y < 0 or y >= n or M[x][y] == 0:
            return 0
        
        M[x][y] = 0
        c[0] += 1
        self.dfs(x+1, y, m, n, M, c)
        self.dfs(x-1, y, m, n, M, c)
        self.dfs(x, y+1, m, n, M, c)
        self.dfs(x, y-1, m, n, M, c)
        
        