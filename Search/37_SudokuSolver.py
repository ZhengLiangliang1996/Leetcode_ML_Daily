class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #按照数独解题依据，判断　横竖和box 枚举+dfs+backtrack

        rows = [[0 for i in range(10)] for j in range(9)]
        cols = [[0 for i in range(10)] for j in range(9)]
        boxes = [[0 for i in range(10)] for j in range(9)]

        # 初始化board 不为.则已经有数字　用１表示
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if(c != '.'):
                    n = int(c)
                    bx = j // 3
                    by = i // 3
                    # rows 表示　第i行已经含有数字n 
                    rows[i][n] = 1
                    # cols 表示　第j列已经含有数字n
                    cols[j][n] = 1
                    # eg: 4行8列 row=3 col=7 各除3得到各自属于的块 横着数的话就是y*3 +bx得到相应的box
                    boxes[by * 3 + bx][n] = 1
        
        self.fill(board, 0, 0, rows, cols, boxes)

    def fill(self, board, x, y, rows, cols, boxes):
        # 当 行到9 就是第十列的时候 说明结束了
        if y == 9:
            return True
        
        #从第一行第一列开始 每次像右边移一格
        nx = (x + 1) % 9
        if (nx == 0): 
            ny = y + 1 
        else:
            ny = y 

        if(board[y][x] != '.'):
            return self.fill(board, nx, ny, rows, cols, boxes)

        for i in range(1,10):
            bx = x // 3
            by = y // 3
            box_key = by * 3 + bx
            #横竖box都没有 
            if(not rows[y][i] and not cols[x][i] and not boxes[box_key][i]):
                rows[y][i] = 1
                cols[x][i] = 1
                boxes[box_key][i] = 1
                board[y][x] = str(i)
                if(self.fill(board, nx, ny, rows, cols, boxes)):
                    return True
                # if not then backtraoking
                board[y][x] = '.'
                boxes[box_key][i] = 0
                cols[x][i] = 0
                rows[y][i] = 0
        return False



def main():
    S = Solution()

    board = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9'],
    ]

    S.solveSudoku(board)

    print(board)
    

if __name__ == "__main__":
    main()
