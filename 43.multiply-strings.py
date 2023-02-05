#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len1 = len(num1)
        len2 = len(num2)
        sum_ = 0
        for i in range(len1):
            for j in range(len2):
                sum_ += (int(num1[len1 - i - 1])*10**(i)) * int(num2[len2 - j - 1])*10**(j)
        res_str = ""
        while(sum_ > 0):
            res_str = str(sum_%10) + res_str
            sum_ = sum_ // 10
        return res_str
# @lc code=end

