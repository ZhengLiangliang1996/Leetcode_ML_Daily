class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
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