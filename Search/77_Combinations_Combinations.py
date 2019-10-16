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
            
            for i in range(index,n+1): # 笔记 去掉index 和不去掉index
                curr.append(i)
                dfs(i+1, curr)         # 笔记 去掉+1和不去掉+1
                curr.pop()

               
        # def dfs(index, curr):
        #     if len(curr) == k:
        #         res.append(curr[:])
        #         return 
            
        #     # 上面的for 代表 1,2,3,4      
        #     for i in range(index+1, n+1):
        #         dfs(i, curr + [i])
                        
        
        dfs(1, [])
        
        return res


def main():

    n = 4
    k = 2
    S = Solution()
    a =  S.combine(4, 2)
    print(a)

if __name__ == "__main__":
    main()
        