class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        n = len(A)
        
        keep = [float('inf')] * n
        swap = [float('inf')] * n
        
        swap[0] = 1
        keep[0] = 0
        
        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap[i] = min(swap[i], keep[i - 1] + 1)
                keep[i] = min(keep[i], swap[i - 1])
                
        return min(keep[n - 1], swap[n - 1])
    
                
        