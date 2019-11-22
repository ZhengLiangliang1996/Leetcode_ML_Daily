class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 0:
            return 0
        
        # 数组dp[x]表示以x结尾的子序列中最长子序列的长度
        # 数组dz[x]表示以x结尾的子序列中最长子序列的个数
        
        lis = [1] * n
        lisn = [1] * n     
        
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lis[j] + 1 > lis[i]:
                        #若不比前面的大　lis[i]将一直维持在１
                        lis[i] = lis[j] + 1
                        lisn[i] = lisn[j]
                    
                    elif lis[j] + 1 == lis[i]:
                        lisn[i] += lisn[j]
                        
        
        # 还要计算出最长子串的个数
        max_lis = max(lis)
        
        total = 0 
        for l,n in zip(lis, lisn):
            if l == max_lis:
                total += n
                
        return total