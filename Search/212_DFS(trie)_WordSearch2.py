class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        if not board: 
            return False

        # build Trie tree 
        trie = {}
        for w in words:   
            t = trie
            for c in w: 
                if c not in t: 
                    t[c] = {}
                t = t[c]
            t['#'] = '#'

        self.res = []
        n = len(board)
        m = len(board[0])
        # mark all the element as not visited
        self.visited = [ [False] * len(board[0]) for i in range(len(board))]
        for i in range(0, n):
            for j in range(0, m):
                self.DFS(board, i, j, trie, '')
        
        return self.res
    
    # pre: element in word, will be extended by using '+' operator with tmp
    def DFS(self, board, i, j, trie, pre):
        # end condition all the letter have been found in the trie 
        if '#' in trie:
            if pre not in self.res:
                self.res.append(pre)

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
            
        if not self.visited[i][j] and board[i][j] in trie:
           tmp = board[i][j]               # matched, should be marked as visited, save in temporary variable
           self.visited[i][j] = True       # marked as visited
           self.DFS(board, i + 1, j, trie[tmp], pre + tmp) 
           self.DFS(board, i - 1, j, trie[tmp], pre + tmp)
           self.DFS(board, i, j + 1, trie[tmp], pre + tmp) 
           self.DFS(board, i, j - 1, trie[tmp], pre + tmp)
           self.visited[i][j] = False       # backtrack
        
def main():
    S = Solution();
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ];

    words = ["oath","pea","eat","rain",""]

    # board = [["a"],["a"]]
    # words = ["aaa"]
    
    a = S.findWords(board, words)

    print(a)
    

if __name__ == "__main__":
    main()

