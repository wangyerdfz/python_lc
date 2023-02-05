#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return None
        idx_1 = m - 1
        idx_2 = n - 1
        idx_total = m + n - 1
        while(idx_2 >= 0 or idx_1 >= 0):
            if idx_2 < 0:
                nums1[idx_total] = nums1[idx_1]
                idx_total -= 1
                idx_1 -= 1
            elif idx_1 < 0:
                nums1[idx_total] = nums2[idx_2]
                idx_total -= 1
                idx_2 -= 1
            else:
                if nums1[idx_1] > nums2[idx_2]:
                    nums1[idx_total] = nums1[idx_1]
                    idx_total -= 1
                    idx_1 -= 1
                else:
                    nums1[idx_total] = nums2[idx_2]
                    idx_total -= 1
                    idx_2 -= 1

        

# @lc code=end

