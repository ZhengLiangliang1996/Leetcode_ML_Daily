class Solution(object):
    def canFinish(self, n, p):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # topological sorting + dfs
        graph = collections.defaultdict(list)
        
        for u, v in p:
            graph[u].append(v)
            
        visited = n * [0]
        
        for i in range(n):
            if not self.dfs(graph, visited, i):
                return False
        
        return True
    
    def dfs(self, graph, visited, i):
        # visited[i] = 1 visiting vistied[i] == visited
        
        if visited[i] == 1:
            return False
        
        if visited[i] == 2:
            return True
        
        visited[i] = 1
        for new in graph[i]:
            if not self.dfs(graph, visited, new):
                return False
        
        visited[i] = 2
        
        return True
    