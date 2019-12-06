class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        isPalindrome = lambda s: s == s[::-1]
        #跳过一个字母
        strPart = lambda s, x: s[:x] + s[x+1:] 
        
        low = 0
        high = len(s) - 1
        
        while low < high:
            if s[low] != s[high]:
                return isPalindrome(strPart(s, low)) or isPalindrome(strPart(s, high))
            
            low += 1
            high -= 1
        return True
    