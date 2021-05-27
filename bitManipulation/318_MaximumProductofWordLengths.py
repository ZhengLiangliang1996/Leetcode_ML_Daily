class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # TLE 
        '''
        
        maxProduct = 0
        if not words:
            return maxProduct
        
        words_uniq = list(set(words))
        words_uniq = sorted(words_uniq, key=len)
        
        def compare(s1, s2):
            sht = sorted(s1)
            for i in range(len(sht)):
                if sht[i] in s2:
                    return False          
            return True 
        print(words_uniq)
        for i in range(len(words_uniq)-1, 0, -1):
            for j in range(i-1, -1, -1):
                if compare(words_uniq[i], words_uniq[j]):
                    print(words_uniq[i], words_uniq[j])
                    maxProduct = max(maxProduct, len(words_uniq[i]) * len(words_uniq[j]))
            
        return maxProduct
        
        '''
        # Compute all masks for all words, we will use d[word] |= 1<<(ord(l) - 97) for this, where 97 is code of symbol a. Also we use | (or) here to update zero-elements, but if we have one-elements, they will not change.
        #Bit Mask 
        res = 0
        d = collections.defaultdict(int)
        N = len(words)
        for i in range(N):
            w = words[i]
            for c in w:
                d[w] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not d[words[j]] & d[words[i]]:
                    res = max(res, len(words[j]) * len(words[i]))
        return res
        
        
