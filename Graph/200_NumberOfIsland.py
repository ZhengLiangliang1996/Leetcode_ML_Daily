class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        dirs = [0, -1, 0, 1, 0]

        def dfs(x,y):
            if x < 0 or x >= m or  y < 0 or y >= n or grid[x][y] != "1":
                return 
            else:
                grid[x][y] = "2"
                for i in range(4):
                    new_x = x + dirs[i]
                    new_y = y + dirs[i+1]
                    dfs(new_x, new_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j) 
                    res += 1        
        return res 
