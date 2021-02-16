class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        '''
In this problem we need to generate all possible letter case permutations, and let us first underatand how many of them we have. If we have digit, we have only 1 option: we need to choose this digit. If we have letter: we have 2 options: choose either small or capital letter. So, if we have m letters, there will be O(2^m) different solutions. When you have a lot of different solutions, it is is a good indicator that it is backtracking problem.
        '''
        res = []

        def dfs(curr, index):
            if len(curr) == len(S):
                res.append(curr)
                return

            if not S[index].isalpha():
                dfs(curr + S[index], index + 1)
            else:
                # 先插入原本
                dfs(curr + S[index], index + 1)
                # 再转大小写
                dfs(curr + chr(ord(S[index]) ^ (1 << 5)), index + 1)

        dfs('', 0)

        return res
