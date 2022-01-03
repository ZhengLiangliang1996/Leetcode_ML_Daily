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

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(s):
            ''' See if string contains valid parentheses 
            '''
            l,r = 0, 0
            for sub in s:
                if sub == "(":
                    l += 1
                elif sub == ')' and l == 0:
                    r += 1
                elif sub == ')' and l != 0:
                    l -= 1
            
            return l, r
        res = []
        
        def dfs(s, l, r, start):
            if l == 0 and r == 0:
                l1, r1 = valid(s)
                if l1 == 0 and r1 == 0:
                    res.append(s)
                    return 
                
            for i in range(start, len(s)):
                if i > start and s[i] == s[i-1]: continue
                
                if s[i] == '(' and l > 0:
                    dfs(s[:i] + s[i+1:], l-1, r, i)
                if s[i] == ')' and r > 0:
                    dfs(s[:i] + s[i+1:], l, r-1, i)
                    
                
            
        l, r = valid(s)
        dfs(s, l, r, 0)
        return res
            
            
            

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def valid(s):
            l = 0
            r = 0
            for i in s:
                if i == "(":
                    l += 1
                elif l != 0 and i == ")":
                    l -= 1
                elif l == 0 and i == ")":
                    r += 1
        
            return l, r
            
        def backtrack(s, l, r, stt):
            if l == 0 and r == 0:
                l1, r1 = valid(s)
                if l1 == 0 and r1 == 0:
                    res.append(s)
                    return
            
            for i in range(stt, len(s)):
                if i > stt and s[i] == s[i - 1]:
                    continue
                    
                if s[i] == ")" and r > 0:
                    path = s[:i] + s[i+1:]
                    backtrack(path, l, r-1, i)
                if s[i] == "(" and l > 0:
                    path = s[:i] + s[i+1:]
                    backtrack(path, l-1, r, i)

        l, r = valid(s)
        backtrack(s, l, r, 0 )
        return res

def main():
    S = Solution();
    a = S.removeInvalidParentheses("(a)())()")
    print(a)

if __name__ == "__main__":
    main()
