class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = [] 
        
        def dp(s, m, wordDict):
            if s in m:
                return m[s]
            
            res = []
            if s in wordDict:
                res.append(s)
            
            for i in range(1, len(s)):
                r = s[i:]
                if r not in wordDict: continue
                    
                res += [w + " " + r for w in dp(s[0:i], m, wordDict)]
            
            m[s] = res
            return m[s]
        
        return dp(s, {}, set(wordDict))
def main():
    S = Solution()
    a = S.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"])
    print(a)

if __name__ == "__main__":
    main()