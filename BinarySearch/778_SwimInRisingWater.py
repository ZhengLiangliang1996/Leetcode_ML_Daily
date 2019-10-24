class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        
        l = 0
        r = n * n
        
        # bfs see if this cell could reach final end 
        def bfs(mid):
            if grid[0][0] > mid:
                return False
            
            q = []
            seen = [0 for i in range(n*n)]
            
            q.append(0)
            seen[0] = 1
            
            # search in for different direction 
            while q:
                a = q.pop(0)
                x = a // n
                y = a % n
                # end condition 
                if x == n - 1 and y == n - 1:
                    return True
                for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    # 越界 或 不符合
                    if a < 0 or b <0 or a >=n or b >=n or grid[a][b] > mid:
                        continue
                        
                    # 符合条件 访问过
                    key = a * n + b
                    if seen[key]:
                        continue
                    # 未访问过 入队
                    seen[key] = 1
                    q.append(key)
            return False
                    
        
        # binary search
        while(l < r):
            mid = l + (r - l) // 2
            
            if bfs(mid):
                r = mid 
            else:
                l = mid + 1
        
        return l