class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res+= 1
                    self.dfs(i, j, m, n, grid)
        
        return res
        
    def dfs(self, x, y, m, n, grid):
        # end condition
        if x >= m or x < 0 or y >=n or y < 0 or grid[x][y] == '0':
            return 
        
        grid[x][y] = '0'
        self.dfs(x+1, y, m, n, grid)
        self.dfs(x-1, y, m, n, grid)
        self.dfs(x, y+1, m, n, grid)
        self.dfs(x, y-1, m, n, grid)
        
        
        