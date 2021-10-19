class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [] 
        
        nums.sort()
        
        def dfs(curr, index):
            # if curr not in res:
            res.append(curr)
            
            for i in range(index, len(nums)):
                # disallow same elements in the same depth
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                dfs(curr + [nums[i]], i+1)
        dfs([], 0)

        return res

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        def backtrack(path, stt):
            res.append(path)
            
            for i in range(stt, len(nums)):
                if i > stt and nums[i] == nums[i-1]:
                    continue
                backtrack(path + [nums[i]], i+1)
        
        nums.sort()
        backtrack([], 0)
        return res 
                
def main():

    input = [1, 2, 2]
    S = Solution()
    a = S.subsetsWithDup(input)
    print(a)

if __name__ == "__main__":
    main()
