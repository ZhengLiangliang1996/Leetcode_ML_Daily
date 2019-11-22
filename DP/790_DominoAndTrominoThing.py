class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # 创建该二数组
        Kmod = 1000000007
        
        f = [[0 for i in range(3)] for j in range(N+1)]
        
        f[0][0] = 1
        f[1][0] = 1
        
        
        for i in range(2, N+1):
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i-1][1] + f[i - 1][2]) % Kmod
            f[i][1] = (f[i - 2][0] + f[i-1][2]) % Kmod
            f[i][2] = (f[i - 2][0] + f[i-1][1]) % Kmod
            
        
        return f[N][0]
    
    
            
        
        
        