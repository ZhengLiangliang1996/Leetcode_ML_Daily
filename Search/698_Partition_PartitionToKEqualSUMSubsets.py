class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        # calculate the sum 
        sum = 0
        for i in range(len(nums)):
            sum = nums[i]
        
        # sort nums to make same elment adjacent
        nums.sort()

        if sum % k != 0:
            return False
        
        # 对used 做移位运算而不是用number的意义　
        # 不需要backtracking 
        def dfs(nums, target, cur, k, used):
            # end condition, number of subset becomes 0
            if k == 0:
                return used == (1 << len(nums)) - 1

            # element 每个都需要扩展
            for i in range(len(nums)):
                if(used & (1 << i)):
                    continue
                t = cur + nums[i]
                new_used = used | (1 << i)
                if(t == target and dfs(nums, target, 0, k - 1, new_used)):
                    return True
                elif(dfs(nums, target, t, k, new_used)):
                    return True
            return False
    

def main():

    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    S = Solution()
    a = S.canPartitionKSubsets(nums, k)
    print(a)
    # print(a)

if __name__ == "__main__":
    main()
