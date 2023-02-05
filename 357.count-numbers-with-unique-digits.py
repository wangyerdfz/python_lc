#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 10
        for i in range(2, n+1):
            c_without_0 = 1
            for j in range(i):
                c_without_0 *= (9 - j)
            c_with_0 = (i -1)
            for j in range(i-1):
                c_with_0 *= (9-j)
            res[i] = res[i-1] + c_without_0 + c_with_0


        return res[-1]
            

# @lc code=end

