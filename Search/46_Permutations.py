# Review
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return res
        used = [0] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return

            for i in range(len(nums)):
                if used[i]: continue

                used[i] = 1
                backtrack(path+[nums[i]])
                used[i] = 0

        backtrack([])
        return res

def main():

    candidates = [1, 2, 3]
    S = Solution()
    a = S.permute(candidates)
    print(a)

if __name__ == "__main__":
    main()

