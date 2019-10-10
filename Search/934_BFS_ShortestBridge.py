class Solution(object):
    def shortestBridge(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # 重点 ： 只有两个小岛 每个小岛里面的1是连接的，先找到一个小岛
        cols = len(matrix[0])
        rows = len(matrix)

        # multi starting points and multi end points, the only thing we need to do is to 
        # add all the starting points to queue and using BFS to find end points 

        # stack = [] save all the starting points into the stack
        stack = []
        # first we need to use DFS to find all the starting point and maked as 2
        
        found = False
        for i in range(rows):
            for j in range(cols):
                # only consider the connected 1
                if matrix[i][j] == 1:
                    self.dfs(i, j, rows, cols, matrix, stack)
                    # reason of using found flag: we only need to mared first island we found
                    found = True
                    break
            if found:
                break


        # using BFS to find the end point where values are equal to 1
        # step = 0
        # while stack:
        #     x, y = stack[0]
        #     stack.pop(0)

        #     for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        #         if a<0 or b<0 or a>=rows or b>=cols or matrix[a][b] == 2:
        #             continue
        #         if matrix[a][b] == 1:
        #             return step
        #         matrix[a][b] = 2
        #         stack.append((a, b))

        #     step += 1

        # return -1

                # -----------
        # breadth first search, once we find next '1', that is our final answer 
        # -----------
        steps = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 和以往的一个wile 一个for不一样 每个elemnt向外扩张一次的bfs算一个step 层层递进
        while stack:
            size = len(stack)
            level = []
            while(size):
                temp = stack.pop()
                size-=1
                x, y = temp[0], temp[1]
                for dx, dy in dirs:
                    tx = x+dx
                    ty = y+dy
                    if tx<0 or ty<0 or tx>=rows or ty>=cols or matrix[tx][ty]==2:
                        continue
                    if matrix[tx][ty]==1:
                        return steps
                    matrix[tx][ty]=2
                    level.append((tx, ty))
            steps+=1
            stack = level
        return -1 


    # using dfs to find the first island 
    def dfs(self, x, y, r, c, matrix, stack):
        # end condition point is not 1
        if x < 0 or x >= r or y < 0 or y >= c or matrix[x][y] != 1:
            return 
        
        matrix[x][y] = 2
        stack.append((x, y))

        # recursion 
        self.dfs(x + 1, y, r, c, matrix, stack)
        self.dfs(x - 1, y, r, c, matrix, stack)
        self.dfs(x, y + 1, r, c, matrix, stack)
        self.dfs(x, y - 1, r, c, matrix, stack)

        

def main():
    S = Solution();

    matrix = [[0,1,0],[0,0,0],[0,0,1]]

    a = S.shortestBridge(matrix)

    print(a)

if __name__ == "__main__":
    main()




