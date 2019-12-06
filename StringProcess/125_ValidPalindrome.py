class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            if not s[i].isdigit() and not s[i].isalpha() and s[i]!=" ":
                s = s.replace(s[i], " ")
        
        s = s.replace(" ","", s.count(" "))
        
        return s[::-1].lower() == s.lower()