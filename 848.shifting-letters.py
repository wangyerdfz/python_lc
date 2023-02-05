#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        if n <= 0:
            return ""
        agg_shifts = [0]*n
        agg_shifts[-1] = shifts[-1]
        for i in range(n-2, -1, -1):
            agg_shifts[i] = agg_shifts[i+1] + shifts[i]

        res_s = ""
        for idx, c in enumerate(s):
            old_val = ord(c) - ord('a')
            new_val = (old_val + agg_shifts[idx]) % 26
            new_char = chr(new_val + ord('a'))
            res_s += new_char

        return res_s
            
# @lc code=end

