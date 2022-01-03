class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(left, right, string, res):
            if left == 0 and right == 0:
                res.append(string)
                return 
            
            if left > 0:
                backtrack(left - 1, right, string + "(", res)
            if right > left:
                backtrack(left , right - 1, string + ")", res)
        
        backtrack(n, n, '',res)
        return res

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [] 
        def dfs(path, left, right):
            if left < 0 or right < 0: return 
            if left == 0 and right == 0:
                res.append(path)
                return 
            
            if left > 0:
                dfs(path + "(", left - 1, right)
            
            if left < right and right > 0:
                dfs(path + ")", left, right - 1)
        
        dfs("", n, n)
        
        return res 
            
            
            
def main():
    S = Solution()
    res = S.generateParenthesis(4)
    print(res)
    

if __name__ == "__main__":
    main()
