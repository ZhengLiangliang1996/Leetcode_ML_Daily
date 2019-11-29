class Solution(object):
    def findOrder(self, n, p):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        res = []
        
        visited = [0] * n
        
        for u,v in p:
            graph[u].append(v)
            
        for i in range(n):
            if not self.dfs(graph, visited, res, i):
                return []
        
        return res
    
    def dfs(self, graph, visited, res, i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        
        for new in graph[i]:
            if not self.dfs(graph, visited, res, new):
                return False
        
        visited[i] = 2
        res.append(i)
        
        return True
        
        
        