import math
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.res = 0
        used = [0 for i in range(len(A))]
        A.sort()

        def squareful(x, y ):
            num = x + y
            root = int(math.sqrt(num))
            if root * root != num:
                return False
            
            return True
        
        def dfs(curr,res):
            if  len(curr) == len(A):
                self.res += 1
                return
            
            for i in range(len(A)):
                if used[i]:
                    continue
                # don't want duplidates 
                if i > 0 and A[i] == A[i-1] and not used[i - 1]:
                    continue
                if curr != [] and not squareful(curr[len(curr)-1], A[i]):
                    continue
      
                used[i] = 1
                dfs(curr+[A[i]], self.res)
                used[i] = 0   
            
        
        dfs([], self.res)
        return self.res
        
            
        
        

def main():

    candidates = [1,1,8,1,8]
    S = Solution()
    a = S.numSquarefulPerms(candidates)
    print(a)
    # print(a)

if __name__ == "__main__":
    main()
