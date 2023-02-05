#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        max_ = 0
        left = 0
        right = n - 1
        while(left < right):
            max_ = max(max_, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_
        # left_max = [-1] * n
        # left_idx = [-1] * n
        # right_max = [-1] * n
        # right_idx = [-1] * n


        # left_max[0] = height[0]
        # left_idx[0] = 0
        # idx = 1
        # while idx < n:
        #     if height[idx] > left_max[idx]:



        # left = 0
        # right = n - 1
        # max_ = -1
        # while(left < right):
        #     cur_water = min(height[left], height[right]) * (right - left)
        #     max_ = max(cur_water, max_)
        #     if(height[left] > height[right]):
        #         right -= 1
        #     else:
        #         left += 1

        # return max_


        # # two pointer
        # n = len(height)
        # if n <= 1:
        #     return 0
        # i = 0
        # j = n - 1
        # max_ = 0
        # while(i <= j):
        #     max_ = max(max_, min(height[i], height[j]) * (j - i))
        #     if height[i] < height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return max_

        # n = len(height)
        # if n <= 1:
        #     return 0
        # max_ = 0
        # left = 0
        # right = n - 1
        # while(left < right):
        #     max_ = max(max_, min(height[left], height[right]) * (right - left))
        #     if height[left] > height[right]:
        #         right -= 1
        #     else:
        #         left += 1
        
        # return max_

        # # smart way :
        # n = len(height)
        # if n == 1:
        #     return 0
        # # step one : get the maximum?
        # max_height = -1
        # for temp_height in height:
        #     if temp_height > max_height:
        #         max_height = temp_height
        # if max_height == 0:
        #     return 0
        # max_water = 0
        # # try height = 1
        # left_iter = 0
        # right_iter = n - 1
        # # for left_iter in range(1, n):
        # #     if height[left_iter] >= 1:
        # #         break
        # # for right_iter in reversed(range(1, n)):
        # #     if height[right_iter] >= 1:
        # #         break
        # # if left_iter >= right_iter:
        # #     return 0
        # # max_water = max(max_water, right_iter - left_iter)
        # for temp_height in range(1, max_height + 1 ):
        #         # move right to find the first
        #     while(left_iter < n):
        #         if height[left_iter] >= temp_height:
        #             break
        #         left_iter+=1
        #     while(right_iter > 0):
        #         if height[right_iter] >= temp_height:
        #             break
        #         right_iter-=1
        #     if left_iter >= right_iter:
        #         return max_water
        #     max_water = max(temp_height * (right_iter - left_iter), max_water)

        # return max_water
                
        # brute force : time limit exceeded
        # water = -1
        # n = len(height)
        # for i in range(n):
        #     for j in range(i,n):
        #         curr_area = min(height[i], height[j])*(j - i)
        #         water = max(water, curr_area)
        # return water


# @lc code=end

