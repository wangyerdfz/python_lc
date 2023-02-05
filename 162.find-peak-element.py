#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0
        if n == 2:
            if nums[0] > nums[1]:
                return 0
            return 1

        if nums[1] < nums[0]:
            return 0
        if nums[n-2] < nums[n-1]:
            return n-1

        def if_peak(i): # 0 : its peak, 1 : left is higher, -1 : right is higher
            if i == 0:
                if nums[i] > nums[i+1]:
                    return 0
                return -1
            if i == n-1:
                if nums[i] > nums[i-1]:
                    return 0
                return 1
            if nums[i] < nums[i-1]:
                return 1
            if nums[i] < nums[i+1]:
                return -1
            return 0


        left = 0
        right = n-1
        while(left < right):
            mid = left + (right - left) // 2
            if if_peak(mid) == 0:
                return mid
            if if_peak(mid) == 1:
                right = mid
            else:
                left = mid + 1

        return left
            
            
            

        
        
# @lc code=end

