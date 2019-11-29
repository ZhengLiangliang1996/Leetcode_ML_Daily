class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
        
        n = len(graph)
        visited = [0] * n
        
        res = []
        for i in range(n):
            if self.dfs(graph, visited, i):
                res.append(i)
                
        res.sort()
        return res
    
    def dfs(self, graph, visited, i):
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