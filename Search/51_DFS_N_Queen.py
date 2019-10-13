class Solution(object):
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 定义存储的变量的数据结构
        res = []
        board = [["." for i in range(n)]for i in range(n)]
        cols = [0 for i in range(n)]
        diag = [0 for i in range(2 * n - 1)]
        diag2= [0 for i in range(2 * n - 1)]

        

        def available(x, y, n):
            # colum and diagonal left is x + y, the symmetric side is x - y + n - 1
            return not cols[x] and not diag[x + y] and not diag2[x - y + n - 1] 

        def updateBoard(x, y, n, is_put):
            cols[x] = is_put
            diag[x + y] = is_put
            diag2[x - y + n - 1] = is_put
            # 这里需要修改
            if is_put:
                board[y][x] = 'Q'
            else:
                board[y][x] = '.'

    #花花用y来表示行是因为从笛卡尔坐标系来思考 
        def nqueens(n, y):
        # end condition
            if(y == n):
            # found one solutions and add that 
                #
                
                res.append(["".join(i) for i in board])
                return 

            # try every colum: 和sudoku一样的步骤 进行搜索列
            for x in range(n):
                # can not put, then stop this time
                if(not available(x, y, n)):
                    continue
                # else 
                updateBoard(x, y, n, True)
                # search next row
                nqueens(n, y+1)
                # back track 清空 
                updateBoard(x, y, n, False)


        nqueens(n, 0)
        
        return res

def main():
    S = Solution()
    a = S.solveNQueens(4)
    print(a)
    
    

if __name__ == "__main__":
    main()