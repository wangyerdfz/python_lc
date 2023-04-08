#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if i == target:
                return True
            
        return False
        # n = len(nums)
        # if n  == 0:
        #     return -1
        # if n == 1 :
        #     if nums[0] == target:
        #         return True
        #     else:
        #         return False
        # def access_val(idx):
        #     return nums[(idx + n)%n]
        

        

        


            
        # # use log n to find the minimum
        # min_idx = -1
        # left = 0
        # right = n-1
        # while(left < right):
        #     if access_val(left-1) > access_val(left):
        #         min_idx = left
        #         break
        #     elif access_val(right-1) > access_val(right):
        #         min_idx = right
        #         break
        #     mid = left + (right - left) // 2
        #     if access_val(mid-1) > access_val(mid):
        #         min_idx = mid
        #         break
        #     if access_val(mid+1) < access_val(mid):
        #         min_idx = mid+1
        #         break
        #     if access_val(mid) > access_val(left): # min on the right side
        #         left = mid + 1
        #     else:
        #         right = mid
        # new_min_idx = min_idx
        # for i in range(min_idx-1, -1, -1):
        #     if nums[i] == nums[min_idx]:
        #         new_min_idx = i
        #     else:
        #         break
        



        # low = 0
        # high = n - 1
        # if nums[(high + new_min_idx)%n] == target or nums[(low + new_min_idx)%n] == target:
        #     return True

        # while(low < high):
        #     mid = low + (high - low) //2
        #     if nums[(mid + new_min_idx)%n] == target:
        #         return True
        #     if nums[(mid + new_min_idx)%n] > target:
        #         high = mid
        #     else:
        #         low = mid + 1
        # return ( low == high) and (nums[(low+ new_min_idx)%n] == target)


# @lc code=end

