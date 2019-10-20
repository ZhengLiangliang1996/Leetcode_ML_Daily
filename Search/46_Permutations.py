# Review 

class Solution(object):
	def permute(self, nums):
		res = []
		# rongcuo 
		if len(nums) == 0:
			return []
		
		used = [0 for i in range(len(nums))]

		def dfs(curr, index):
			if len(curr) == len(nums):
				res.append(curr)
				return 
			for i in range(index, len(nums)):
				# if used[i]:
					# continue
				# if not used[i]:
					# used[i] = 1
				dfs(curr + [nums[i]], i+1)
					# used[i] = 0				
		
		dfs([], 0)
		return res


def main():

    candidates = [1, 2, 3]
    S = Solution()
    a = S.permute(candidates)
    print(a)

if __name__ == "__main__":
    main()

