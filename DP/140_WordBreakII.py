class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        def dp(s, m, wordDict):
            if s in m:
                return m[s]
            
            res = []
            if s in wordDict:
                res.append(s)
                
            for i in range(len(s)):
                r = s[i:]
                if r not in wordDict: continue
                
                res += [w + " " + r for w in dp(s[0:i], m, wordDict)]
            
            m[s] = res
            return m[s]
        
        
        return dp(s, {}, set(wordDict))