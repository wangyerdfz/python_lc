#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        buffer = ''
        for c in s:
            if c != ' ':
                buffer = c + buffer
            else:
                res += buffer
                res += c
                buffer = ""

        if len(buffer) > 0:
            res += buffer
        return res
# @lc code=end

