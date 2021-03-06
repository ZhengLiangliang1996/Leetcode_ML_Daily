class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # BFS SHORTEST distance  4 wheel up and down and there are 2 * 4 = 8 different ways to expand the search space        
        # set the dead list 
        dead = set(deadends)
        if "0000" in dead:
            return -1
        dead.add("0000")
        # initialize the queue with wheel: 0000 dist = 0
        q = [("0000", 0)]
    
        while len(q) > 0:
            currentwheel, dist = q.pop(0)
            if currentwheel == target:
                return dist

            neighbour = self.findNeighbour(currentwheel, dist+1, dead)

            if len(neighbour)>0:
                q.extend(neighbour)
    
        return -1
    # search the wheel
    def findNeighbour(self, currentwheel, dist, dead):
        # return the currentwheel number 
        output = []


        #实现细节：dist+1 这里　在这个部分的dist都只+1 因为是搜索了所有的结果　但是始终只用了一步
        for i in range(4):
            num = int(currentwheel[i])
            for a in ((num-1), (num+1)):
                tmp = currentwheel[:i] + str(a%10) + currentwheel[i+1:]

                # check if this is a valid step
                if tmp not in dead:
                    output.append((tmp, dist))
                    dead.add(tmp)
        return output




def main():
    S = Solution()

    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"

    a = S.openLock(deadends, target)
    print(a)
    
if __name__ == "__main__":
    main()

