class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # create queue and enqueue first point
        tree = []

        cols = len(forest[0])
        rows = len(forest)

        #put height into 
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1:
                    tree.append((forest[i][j], i, j))

        def takeFirst(elem):
            return elem[0]
        # sort by height 
        tree.sort(key=takeFirst)

        sx = 0
        sy = 0

        totalStep = 0

        # BFS
        def BFS(forest, sx, sy, tx, ty):
            seen = [[0 for i in range(cols)] for j in range(rows)]

            q = []
            q.append((sx, sy))
            steps = 0

            while q:
                new_nodes = len(q)
                while new_nodes > 0:
                    cx, cy = q.pop(0)

                    # found the shortest path
                    if cx == tx and cy == ty:
                        return steps
                    
                    for x, y in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                        # out of bounds 
                        if(x < 0 or x == rows or y < 0 or y == cols or not forest[x][y] or seen[x][y]):
                            continue
                        
                        # mark x y as visited
                        seen[x][y] = 1
                        q.append((x, y))
            
            return float('inf')

        # Move from current position to next tree to cut
        for i in range(len(tree)):
            tx = tree[i][1]
            ty = tree[i][2]

            steps = BFS(forest, sx, sy, tx, ty)

            if steps == float('inf'):
                return -1

            totalStep = totalStep + steps

            sx = ty
            sy = ty
        
        return totalStep

def main():
    S = Solution()

    #a = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
    a = [
        [1,2,3],
        [0,0,4],
        [7,6,5]
        ]
        
    a1 = S.cutOffTree(a)
    
    print(a1)
    
if __name__ == "__main__":
    main()