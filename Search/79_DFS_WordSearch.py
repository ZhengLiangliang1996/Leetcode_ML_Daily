class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        n = len(board)
        m = len(board[0])
        
        def search(word, word_len, x, y):
            # end condition
            if not board: return False
            # end condition
            if(x < 0 or x == m or y < 0 or y == n or word[word_len] != board[y][x]):
                return False
            
            # found the last char of the words
            if(word_len == len(word) - 1):
                return True
            
            cur = board[y][x]
            board[y][x] = '#'
            found = search(word, word_len + 1, x + 1, y) or search(word, word_len + 1, x - 1, y) or search(word, word_len + 1, x , y + 1) or search(word, word_len + 1, x , y - 1)
            board[y][x] = cur
            return found
        
        for k in words:
            for i in range(0, m):
                for j in range(0, n):
                    if(search(k, 0, i, j)):
                        if k not in res:
                            res.append(k)
        
        return res

def main():
    S = Solution();
    # board = [
    #     ['o','a','a','n'],
    #     ['e','t','a','e'],
    #     ['i','h','k','r'],
    #     ['i','f','l','v']
    # ];

    # words = ["oath","pea","eat","rain",""]

    board = [["a"],["a"]]
    words = ["aaa"]
    
    a = S.findWords(board, words)

    print(a)
    

if __name__ == "__main__":
    main()

