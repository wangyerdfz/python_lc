#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n <= 1:
            return []
        left, right = 0, n - 1
        while(left < right):
            if numbers[left] + numbers[right] < target:
                left+=1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []

        # n = len(numbers)
        # if n <= 1:
        #     return []

        # left, right = 0, n - 1
        # while(left < right):
        #     if numbers[left] + numbers[right] < target:
        #         left += 1
        #     elif numbers[left] + numbers[right] > target:
        #         right -= 1
        #     else:
        #         return [left + 1, right + 1]
            
        # return []
# @lc code=end

