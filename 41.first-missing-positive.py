#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >=n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i]%n] += n
        
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
# @lc code=end

