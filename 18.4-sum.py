#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        pos_dict = {}
        for idx, i in enumerate(nums):
            pos_dict[i] = idx
        res = []
        for i in range(n):
            if 4 * nums[i] > target:
                return res
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if nums[i] + 3*nums[j] > target:
                    continue
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                for k in range(j+1, n):
                    if nums[i] + nums[j] + 2*nums[k] > target:
                        continue
                    if k > j+1 and nums[k-1] == nums[k]:
                        continue
                    if pos_dict.get(target - nums[i] - nums[j] - nums[k], -1) > k:
                        res.append([nums[i], nums[j], nums[k], target - nums[i] - nums[j] - nums[k]])


        return res

# @lc code=end

