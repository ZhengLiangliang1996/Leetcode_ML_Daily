class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # transfer 2d to 1d
        
        if not matrix:
            return False
        
        cols = len(matrix[0])
        
        l = 0
        r = rows * cols - 1
        
        while(l <= r):
            mid = l + ((r - l) // 2)
            print(mid)

            # 
            mid_y = mid % cols  # 重点！ 
            mid_x = mid // cols # 重点！
            print(mid_x, mid_y)
            if matrix[mid_x][mid_y] == target:
                return True
            elif matrix[mid_x][mid_y] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
    

from bisect import bisect,bisect_right,bisect_left

def main():

    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
    S = Solution()
    #a = S.searchMatrix(matrix, 13)
    # bisect 测试 
    data = [2, 2, 3, 4, 9, 7]
    print(bisect(data, 2))
    # print(a)
    # print(a)

if __name__ == "__main__":
    main()
             