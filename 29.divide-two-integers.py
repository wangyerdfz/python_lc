#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math
        res = dividend/divisor
        if res < - 2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 -1
        if res < 0 :
            return int(math.ceil(res))
        else:
            return int(math.floor(res))
# @lc code=end

