class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        candidates = [i for i in range(1, 10)]
        
        def dfs(candidates, target, index, curr):
            # end condition 
            if target == 0 and len(curr) == k:
                res.append(curr)
                return 
            
            # prue 
            if len(curr) > k:
                return 
            
            for i in range(index, 9):
                if target < candidates[i]:
                    return 
                
                dfs(candidates, target - candidates[i], i + 1, curr + [candidates[i]])
        
        dfs(candidates, n, 0, [])
        
        return res
                