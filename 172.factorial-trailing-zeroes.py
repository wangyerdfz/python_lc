#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int: # given 2 is bigger
        base = 5
        res = 0
        while(n // base > 0):
            res += n //base
            base *= 5

        return res
        
# @lc code=end

