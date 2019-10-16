class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(curr, index):
            res.append(curr)
            
            # 扩展
            for i in range(index, len(nums)):
                dfs(curr+[nums[i]], i+1)
            
        
        dfs([], 0)
        
        return res


def main():

    input = [1, 2, 2]
    S = Solution()
    a = S.subsets(input)
    print(a)

if __name__ == "__main__":
    main()
