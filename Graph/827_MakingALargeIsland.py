class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # 存储每个出现的island块的面积
        # 注意color需要从２开始　不然会和其他的１有冲突
        area = dict()
        area[0] = 0
        color = 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    color += 1
                    area[color] = self.dfs(i, j, m, n, color, grid)
                    res = max(area[color], res)
       
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    all_area = 1
                    for color in set([self.get_color(i + 1, j, m, n, grid), self.get_color(i - 1, j, m, n, grid), self.get_color(i, j + 1, m, n, grid), self.get_color(i, j - 1, m, n, grid)]):
                        all_area += area[color]
                
                    res = max(all_area, res)
        
        return res
    
    def dfs(self,x, y, m, n, color, grid):
        if x >= m or x < 0 or y >=n or y < 0 or grid[x][y] != 1:
            return 0
        
        grid[x][y] = color
        return 1 + self.dfs(x + 1, y, m, n, color, grid) + self.dfs(x - 1, y, m, n, color, grid) + self.dfs(x, y + 1, m, n, color, grid) + self.dfs(x, y - 1, m, n, color, grid)
    
    def get_color(self, x, y, m, n, grid):
        return 0 if x < 0 or x >= m or y < 0 or y >=n else grid[x][y]