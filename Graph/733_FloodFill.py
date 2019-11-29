class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        if not image:
            return 0
        
        m = len(image)
        n = len(image[0])
        
        if newColor == image[sr][sc]:
            return image
        
        self.dfs(sr, sc, newColor, m, n, image, image[sr][sc])
        
        return image
        
        
    def dfs(self, x, y, newColor, m, n, image, o):
        if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != o:
            return 
        image[x][y] = newColor
        
        self.dfs(x + 1, y, newColor, m, n, image, o)
        self.dfs(x - 1, y, newColor, m, n, image, o)
        self.dfs(x, y + 1, newColor, m, n, image, o)
        self.dfs(x, y - 1, newColor, m, n, image, o)
        