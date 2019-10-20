class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        # dfs 中的 target 一直被减
        def dfs(candidates, target, index, curr, res):
            # end condition
            if target == 0:
                res.append(curr[:])
                return  

            for i in range(index, len(candidates)):
                if target < candidates[i]:
                    return 
                curr.append(candidates[i])
                dfs(candidates, target - candidates[i], i+1, curr, res)
                curr.pop()
        
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res


def main():

    candidates = [10,1,2,7,6,1,5]
    target = 8
    S = Solution()
    # a = S.combinationSum(candidates, target)
    print(str.isdigits("1"))
    print(a)

if __name__ == "__main__":
    main()
