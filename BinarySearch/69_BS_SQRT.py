class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x 
        
        while(l <= r):
            mid = l + ((r - l) >> 1)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        # 注意要返回 r而不是 l                
        return r



def main():

    x = 22
    S = Solution()
    a = S.mySqrt(x)
    print(a)
    # print(a)

if __name__ == "__main__":
    main()
             