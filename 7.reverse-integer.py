#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)
        res = 0
        while(x > 0):
            res *= 10
            res += (x % 10)
            x = x//10
        if is_neg :
            res = res * -1
        if (res > 2**31 - 1) or (res < - 2**31):
            return 0
        return res
        # sum_ = 0
        # neg = False
        # if x < 0 :
        #     x = -1 * x
        #     neg = True
        # while(x > 0):
        #     sum_ = sum_*10 +  x%10
        #     x = x//10
        # if neg:
        #     sum_ = sum_ * -1
        # if (sum_ <= -1 * 2**31) or (sum_ >= 2**31 -1):
        #     return 0

        # return sum_


        
# @lc code=end

