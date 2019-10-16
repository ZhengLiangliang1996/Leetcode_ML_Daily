class Solution(object):
    def letterCombinations(self, digits):
        
        dict = {}

        if digits == '':
            return []

        dict['2'] = ['a','b','c']
        dict['3'] = ['d','e','f']
        dict["4"] = ['g','h','i']
        dict["5"] = ['j','k','l']
        dict["6"] = ['m','n','o']
        dict["8"] = ['t','u','v']
        dict["7"] = ['p','q','r','s']
        dict["9"] = ['w','x','y','z']

        res = []
        def dfs(curr, index, res):
            if len(curr) == len(digits):
                res.append(curr)
                return

            # 扩展 遍历每个字母 每个字母进行dfs
            
            for i in dict[digits[index]]:
                dfs(curr, index + 1, res)
        dfs("", 0, res)

        return res



def main():

    input = "23"
    S = Solution()
    a = S.letterCombinations(input)
    print(a)

if __name__ == "__main__":
    main()