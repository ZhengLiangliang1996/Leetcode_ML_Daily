class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        cols = [0 for i in range(n)]
        # diagonal total 2 * n - 1 
        diag1 = [0 for i in range(2 * n - 1)]
        diag2 = [0 for i in range(2 * n - 1)]
        n
        # board n * n 
        board = [["." for i in range(n)] for j in range(n)]
        
        
        
        # see if this colum could be put
        def couldBePut(x, y, n):
            # original 0 if all result is 1 (not 0) among cols, diag1 and diag2, return True
            # index of diag1 is x+y and the symmetrical line wrt y axis is x-y+n-1
            return not cols[x] and not diag1[x + y] and not diag2[x - y + n - 1]
        
        # putFlag indicates whether this time is put or backtracking(cleaning)
        def updateBoard(x, y, n, putFlag):
            cols[x] = putFlag
            diag1[x + y] = putFlag
            diag2[x - y + n - 1] = putFlag
            # if could be put
            if putFlag:
                board[y][x] = "Q"
            # clean this position
            else:
                board[y][x] = "."
        
        # numeber of Queen n and Row Number y
        def N_Queen(n, y):
            # end condition when it reached final+1 rows
            if y == n:
                # return result
                res.append(["".join(i) for i in board])
                return
                
            # enumerate from 0~n-1(cols) to see if this could be put into this coloum
            for i in range(n):
                if not couldBePut(i, y, n):
                    continue
                # update the board 
                updateBoard(i, y, n, True)
                # next col recursion
                N_Queen(n, y + 1)
                # backtrack cleaning
                updateBoard(i, y, n, False)
        
        N_Queen(n, 0)
        return res

def main():
    S = Solution()
    res = S.totalNQueens(4)

    print(res)
    

if __name__ == "__main__":
    main()