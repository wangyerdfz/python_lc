#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def __init__(self):
        self.cache = {}

    def numDistinct(self, s: str, t: str) -> int:
        if (s, t) in self.cache:
            return self.cache[(s, t)]
        n_s = len(s)
        n_t = len(t)
        if n_s < n_t:
            self.cache[(s, t)] = 0
            return 0
        if n_t == 0:
            self.cache[(s, t)] = 1
            return 1
        ans_ = 0
        for idx, c in enumerate(s):
            if c == t[0]:
                ans_ += self.numDistinct(s[idx+1:], t[1:])
        self.cache[(s, t)] = ans_
        return ans_
# @lc code=end

