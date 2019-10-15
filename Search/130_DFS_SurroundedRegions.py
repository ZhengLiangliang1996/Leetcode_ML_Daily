class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # 思路 只查找边界 得到的O进行DFS
        if board == []:
            return

        rows = len(board)
        cols = len(board[0])
        
        def dfs(x, y):
            if x<0 or x>=rows or y<0 or y>=cols or board[x][y] != "O": 
                return
            #mark as 'G'
            board[x][y] = "G"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            
        
        # only search boundary
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
            
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)
        
        print(board)
        # check back
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "G":
                    board[x][y] = "O"
        
        print(board)
          

def main():
    S = Solution()

    #a = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
    #a = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    a = []   
    S.solve(a)
    
if __name__ == "__main__":
    main()