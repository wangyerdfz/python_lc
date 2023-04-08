#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_s = 1
        num_set = set(nums)
        if len(num_set) == 0:
            return 0
        for i in num_set:
            cur_streak = 1
            if i-1 in num_set:
                continue
            cur = i + 1
            while(cur in num_set):
                cur_streak += 1
                max_s = max(max_s, cur_streak)
                cur += 1

        return max_s
            



# @lc code=end

