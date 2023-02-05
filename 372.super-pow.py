#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 0:
            return 0
        if a == 1:
            return 1
        b = "".join([str(x) for x in b])
        a = a%1337

        b = int(b)
        res =1
        for _ in range(b):
            res = (res*a)%1337
        return res
# @lc code=end

