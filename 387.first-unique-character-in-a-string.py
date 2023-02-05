#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return -1
        if n == 1:
            return 0
        times_dict = {}
        for c in s:
            times_dict[c] = times_dict.get(c, 0) + 1

        for i in range(n):
            freq = times_dict.get(s[i], 0)
            if freq == 1:
                return i
        
        return -1
        
# @lc code=end

