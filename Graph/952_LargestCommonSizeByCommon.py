class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
      
        parents = list(range(max(A) + 1))
        
        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            
            return x
        
        def un(x, y):
            parents[find(x)] = parents[find(y)]
                
        
        for a in A:
            for k in range(2, int(math.sqrt(a) + 1)):
                if a % k == 0:
                    un(a, k)
                    un(a, a//k)
            
        return collections.Counter([find(a) for a in A]).most_common(1)[0][1]  
        
        