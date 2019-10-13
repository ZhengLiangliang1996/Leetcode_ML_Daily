class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []

        def dfs(left, right, string, res):
            if left == 0 and right == 0:
                res.append(string)
                return 
            
            if left > 0:
                dfs(left - 1, right, string + "(", res)
            if right > left:
                dfs(left , right - 1, string + ")", res)
        
        dfs(n, n, '',res)
        return res


def main():
    S = Solution()
    res = S.generateParenthesis(4)
    print(res)
    

if __name__ == "__main__":
    main()