class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # count how many left and right should be deleted
        l = 0
        r = 0 
        for i in s: 
            l = l + (i == '(')
            # if there is no left 
            if (l == 0): 
                r = r + (i == ')')
            # if there is already a left, and right has been detected, minus 1 of left
            else:
                l = l - (i == ')')
                

        # end condition
        def isValid(s):
            count = 0
            for ch in s:
                if ch == '(': count = count + 1
                if ch == ')': count = count - 1
                if count < 0: return False # means the first two lines are not both fully exercuted
            return count == 0

        # start: the index where we deleted last parenthesis
        def dfs(s, start, l, r, res):
            # end condition
            if l == 0 and r == 0: 
                if isValid(s): 
                    res.append(s)
                    return 
            
            # when care about element is parenthesis
            for i in range(start, len(s)):
                # pruning: remove consecutive if first one is also the same to avoid duplications
                if (i != start and s[i] == s[i - 1]):
                    continue
                # element is parenthesis
                if (s[i] == '(' or s[i] == ')'): 
                    curr = s 
                    curr = curr[:i] + curr[i + 1:]

                    if r > 0:
                        dfs(curr, i, l, r - 1, res)
                    if l >0:
                        dfs(curr, i, l - 1, r, res)

        
        res = []
        dfs(s, 0, l, r, res)
        return res




def main():
    S = Solution();
    a = S.removeInvalidParentheses("(a)())()")
    print(a)

if __name__ == "__main__":
    main()