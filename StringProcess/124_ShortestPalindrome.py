class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s+'#'+s[::-1]
        nex = self.getNext(a)
        print(nex)
        pre = s[nex[len(nex) - 1]+1:]
        pre = pre[::-1]
        return pre+s
        
    def getNext(self, p):
        nex = [0] * len(p)
        nex[0] = -1
        i = 0
        j = -1
        
        while i < len(p) - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                nex[i] = j
            else:
                j = nex[j]
        
        return nex
        
        