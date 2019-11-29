class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        # initialize
        # 去重
        A = list(set(A))
        n = len(A)
        parents = [0] * n
        self.size = n
        
        # all groups point to itself
        for i in range(n):
            parents[i] = i
            
        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        
        # merge 
        def uf(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                parents[x] = y
                self.size -= 1
        
        def similar(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                if count >= 3:
                    return False
                
            return True
        
        for i in range(n):
            for j in range(i + 1, n):
                if similar(A[i], A[j]):
                    uf(i, j)
        
        return self.size
                    
            
        