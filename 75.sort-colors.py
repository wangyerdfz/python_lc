#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return 
        counts = [0,0,0]
        
        for i in range(n):
            counts[nums[i]] += 1
        idx = 0
        for i in range(3):
            while(counts[i] >0):
                nums[idx] = i
                counts[i] -= 1
                idx += 1
        
        return
        

        
        
# @lc code=end

