#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        res = []
        for comb in self.combine(n, k -1):
            for i in reversed(range(1, n +1)):
                if i > comb[0]:
                    res.append([i] + comb)
        return res
# @lc code=end

