#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        swap_idx = -1

        idx = 0
        cur_num = nums[idx]
        cnt = 1
        for idx in range(1, n):
            if nums[idx] == cur_num:
                if swap_idx == -1:
                    swap_idx = idx

            else: # new number
                cur_num = nums[idx]
                if swap_idx == -1: # dont do anything
                    cnt+=1
                else:
                    nums[swap_idx] = nums[idx]
                    swap_idx +=1
                    cur_num = nums[idx]
                    cnt+=1

        return cnt
# @lc code=end

