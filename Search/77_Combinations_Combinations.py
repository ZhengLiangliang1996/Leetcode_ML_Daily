class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 容错处理
        
        res = []
        
        
        def dfs(index, curr):
            if len(curr) == k:
                res.append(curr[:])
                return 
            
            for i in range(index+1,n+1): # 笔记 去掉index 和不去掉index
                curr.append(i)
                dfs(i, curr)         # 笔记 去掉+1和不去掉+1
                curr.pop()

               
        # def dfs(index, curr):
        #     if len(curr) == k:
        #         res.append(curr[:])
        #         return 
            
        #     # 上面的for 代表 1,2,3,4      
        #     for i in range(index+1, n+1):
        #         dfs(i, curr + [i])
                        
        
        dfs(0, [])
        
        return res
# 2021-10-20
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path, k, stt):
            if k == 0:
                res.append(path)
                
            for i in range(stt, n+1):
                backtrack(path + [i], k-1, i+1)
            
        backtrack([], k, 1)
        return res
def main():

    n = 4
    k = 2
    S = Solution()
    a =  S.combine(4, 2)
    print(a)

if __name__ == "__main__":
    main()
        
