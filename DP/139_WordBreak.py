class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        def dp(s, m, wordDict):
            if s in m:
                return m[s]
            
            if s in wordDict:
                m[s] = True
                return True
            
            for i in range(len(s)):
                r = s[i:]
                if r in wordDict and dp(s[0:i], m, wordDict):
                    m[s] = True
                    return True
            m[s] = False
            return False
        
        return dp(s, {}, set(wordDict))
                
        
                