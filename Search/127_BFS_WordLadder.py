import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Enqueue the beginWord, with key step
        q =[(beginWord, 1)]

        history = set()
        history.add(beginWord)
        # if beginWord is a transformed word
        #dict subclass that calls a factory function to supply missing values
        memo = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                memo[word[:i] + "#" + word[i+1:]].append(word)

        while q:
            currWord, dist = q.pop(0)
            # end condtion
            if currWord == endWord:
                return dist

            # search stage
            for i in range(len(beginWord)):
                # currAlphabet
                # a = currWord[i]
                # expand visiting and searching alphabetList
                for x in memo[currWord[:i] + '#' + currWord[i+1:]]:
                    # check if this is a valid word
                    if (x not in history):
                        q.append((x, dist+1))
                        history.add(x)

        return 0

    def LadderLength_v1(self, beginWord, endWord, wordList):
        visited = set(wordList)
        q = collections.deque()
        q.append(beginWord)
        if endWord not in wordList:
            return 0

        step = 0

        while q:

            step = step + 1
            qSize = len(q)

            for k in range(qSize):
                node = q.popleft()
                for i in range(len(node)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        word = node[:i] + j + node[i+1:]
                        if word == endWord and word in visited:
                            return step+1

                        if word not in visited:
                            continue

                        if word != node and word in visited:
                            visited.remove(word)
                            q.append(word)
        return 0

def main():
    S = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    a = S.ladderLength(beginWord,endWord,wordList)

    print(a)

if __name__ == "__main__":
    main()
