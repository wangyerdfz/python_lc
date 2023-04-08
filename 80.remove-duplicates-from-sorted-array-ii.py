#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
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
        cur_num_cnt = 1
        cnt = 1
        for idx in range(1, n):
            if nums[idx] != cur_num or cur_num_cnt <= 1:
                # need to swap
                if nums[idx] != cur_num: # first let's handle cur_num_cnt
                    cur_num_cnt =1
                    cur_num = nums[idx]
                else:
                    cur_num_cnt += 1
                if swap_idx == -1: # if it's already in front, then no need
                    pass
                else: # need to actually swap
                    nums[swap_idx] = nums[idx]
                    swap_idx += 1
                cnt += 1
                
            else:
                # only have to update cur_num_cnt
                cur_num_cnt += 1
                # encounter the first 3-duplicates: create new swap_idx
                if swap_idx == -1:
                    swap_idx = idx

        return cnt






        #     if nums[idx] == cur_num:
        #         cur_num_cnt += 1
        #         if cur_num_cnt <= 
        #         if swap_idx == -1:
        #             swap_idx = idx

        #     else: # new number
        #         if swap_idx == -1: # dont do anything
        #             cnt+=1
        #         else:
        #             nums[swap_idx] = nums[idx]
        #             swap_idx +=1

        #             cur_num = nums[idx]
        #             cnt+=1

        # return cnt


# @lc code=end

