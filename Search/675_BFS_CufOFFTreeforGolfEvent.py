class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # create queue and enqueue first point
        queue = [(0, 0)]

        cols = len(forest[0])
        rows = len(forest)

        step = -1
        zeroN = 0
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] == 0:
                    zeroN = zeroN + 1
        # if the first tree is 0
        if forest[0][0] == 0:
            return step
        
        while queue:
            # pop from queue
            x, y = queue.pop(0)
            
            for (a, b) in [(x+1, y), (x-1, y), (x, y-1), (x, y + 1)]:
                
                if 0<=a<rows and 0<=b<cols and forest[a][b] != 0 and forest[x][y] < forest[a][b]:
                    # enqueue
                    queue.append((a, b))
            step = step + 1

        return step
        # if step+1 == cols*rows - zeroN:
        #     return step
        # else:
        #     return -1

def main():
    S = Solution()

    a = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]

    a1 = S.cutOffTree(a)
    
    print(a1)
    
if __name__ == "__main__":
    main()