#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        for i in range(n):
            res = [[nums[i]] + x for x in res] + res

        return res

        
# @lc code=end

