class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        cols = len(matrix[0])
        rows = len(matrix)

        q = []
        dist = [ [float('inf') for _ in range(cols)] for _ in range(rows)]


        # initialize the distance matrix: reuslt
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # classical bfs structure        
        while q:
            x, y = q[0]
            q.pop(0)

            for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0<=a<rows and 0<=b<cols and dist[a][b]-dist[x][y] > 1:
                    dist[a][b] = dist[x][y] + 1
                    q.append((a, b))
        return dist

def main():
    S = Solution()

    matrix = \
        [[0,0,0],
        [0,1,0],
        [1,1,1]]

    a = S.updateMatrix(matrix)
    print(a)
    
if __name__ == "__main__":
    main()



