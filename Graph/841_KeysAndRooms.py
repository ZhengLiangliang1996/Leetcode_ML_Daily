class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        visited = set()
        
        def dfs(cur):
            # 若已经访问了
            if cur in visited:
                return 
            visited.add(cur)
            for next in rooms[cur]:
                dfs(next)
        
        dfs(0)
        
        return len(visited) == len(rooms)
    
        