#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n < 1:
            return []
        if target == 0:
            return [[]]
        if target < 0:
            return []
        res = []
        for i in range(n):
            tmp_res = self.combinationSum(candidates[i:], target - candidates[i])
            if len(tmp_res) > 0:
                res += [[candidates[i]] + x for x in tmp_res]
        return res
        
# @lc code=end

