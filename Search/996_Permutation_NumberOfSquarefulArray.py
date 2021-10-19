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

class Solution(object):
    def numSquarefulPerms(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        res = []
        if not nums: return 0
        used = [0] * len(nums)
        
        def squreful(x, y):
            z = x + y
            z_sqrt = sqrt(z)
            return int(z_sqrt)**2 == z
        
        def backtrack(path):
            
            if len(path) == len(nums):
                res.append(path)
                
            for i in range(len(nums)):
                if path and not squreful(path[-1], nums[i]):
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    used[i] = 1
                    backtrack(path + [nums[i]])
                    used[i] = 0
        nums.sort()
        backtrack([])
        print(res)
        return len(res)
        
        
    

if __name__ == "__main__":
    main()

