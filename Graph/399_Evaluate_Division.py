class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # solution 1: DFS
#         g = collections.defaultdict(dict)
        
#         # 建有向图图
#         for [x, y], v in zip(equations, values):
#             g[x][y] = v
#             g[y][x] = 1.0 / v
            
#         # dfs
#         def dfs(x, y, visited):
#             if x == y:
#                 return 1.0
#             visited.add(x)
            
#             for n in g[x]:
#                 if n in visited:
#                     continue
#                 visited.add(n)
#                 d = dfs(n, y, visited)
#                 if d>0:
#                     return d * g[x][n]
#             return -1
        
#         ans = [dfs(x, y, set()) if x in g and y in g else -1 for x,y in queries]
        
#         return ans

        # solution2: Union find
        
        # 建图的细节是让中间量成为另外的parents
        
        def find(x):
            if x != U[x][0]:
                px, pv = find(U[x][0])
                U[x] = (px, U[x][1] * pv)
            return U[x]
        
        def divide(x, y):
            px, xv = find(x)
            py, yv = find(y)
            if px != py:
                return -1
            
            return xv / yv

        U = {}
        for [x, y], v in zip(equations, values):
            if x not in U and y not in U:
                U[x] = (y, v)
                U[y] = (y, 1)
            elif x not in U:
                U[x] = (y, v)
            elif y not in U:
                U[y] = (x, 1.0 / v)
            else:
                rx, xv = find(x)
                ry, yv = find(y)
                U[rx] = (ry, v / xv * yv)
                
        
        return [divide(x, y) if x in U and y in U else -1 for x, y in queries]
    