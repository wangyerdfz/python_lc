#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n <= 2:
            return -1
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            j, k = i+1, n-1
            while(j < k):
                sum_ = nums[i] +nums[j] + nums[k]
                if sum_ == target:
                    return target
                if abs(sum_ - target) < abs(closest - target):
                    closest = sum_
                if sum_ > target:
                    k-=1
                else:
                    j+=1

        return closest

# @lc code=end

