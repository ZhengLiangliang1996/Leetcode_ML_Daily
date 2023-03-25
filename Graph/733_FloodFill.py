class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        k = [-1, 1, ]
        dirs = [0,-1,0,1,0]
        cur_cor = image[sr][sc]
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != cur_cor or image[x][y] == color:
                return 
            else:
                image[x][y] = color 
                for i in range(4):
                    new_x = x + dirs[i]
                    new_y = y + dirs[i+1]
                    dfs(new_x, new_y)
        
        dfs(sr, sc)
        return image
