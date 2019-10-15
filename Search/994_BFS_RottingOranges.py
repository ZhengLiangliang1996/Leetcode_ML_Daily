class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        q = []
        
        # find roitting 
        numOne = 0
        numTwo = 0
        numZero = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    numTwo += 1
                    q.append((i, j))
                if grid[i][j] == 1:
                    numOne += 1
                if grid[i][j] == 0:
                    numZero += 1
        
        if numZero + numTwo == rows * cols:
            return 0
        
        # BFS
        step = -1
        while q:
            sizeQ = len(q)
            for i in range(sizeQ):
                x, y = q.pop(0)
                
                for (xx, yy) in [(x+1, y), (x-1,y), (x, y+1), (x, y-1)]:
                    if 0<=xx<rows and 0<=yy<cols and grid[xx][yy] == 1:
                        # mark as visted
                        grid[xx][yy] = 2
                        q.append((xx,yy))
                        numOne -= 1
            step += 1
        
        if not numOne:
            return step
        else:
            return -1