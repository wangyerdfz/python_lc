#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        left_to_right = []
        right_to_left = []
        n = len(nums)
        if n == 1:
            return 1
        last_left = 0
        last_right = 0
        for i in range(n):
            if i%2 == 0:
                last_left += nums[i]
                last_right += nums[n -1 - i]
                left_to_right.append(last_left)
                right_to_left.append(last_right)
            else:
                last_left -= nums[i]
                last_right -= nums[n - 1 -  i]
                left_to_right.append(last_left)
                right_to_left.append(last_right)
        right_to_left = list(reversed(right_to_left))
        right_to_left = [i*(-1)**(n + 1) for i in right_to_left]
        cnt = 0
        for i in range(n):
            if i == 0:
                pre_num = 0
            else: 
                pre_num = left_to_right[i -1]
            if i == n - 1:
                post_num = 0
            else:
                post_num = right_to_left[i + 1]
            if pre_num == post_num:
                cnt+=1

        return cnt


# def fair(nums : list)->int:
#     left_to_right = []
#     right_to_left = []
#     n = len(nums)
#     if n == 1:
#         return 1
#     last_left = 0
#     last_right = 0
#     for i in range(n):
#         if i%2 == 0:
#             last_left += nums[i]
#             last_right += nums[n -1 - i]
#             left_to_right.append(last_left)
#             right_to_left.append(last_right)
#         else:
#             last_left -= nums[i]
#             last_right -= nums[n - 1 -  i]
#             left_to_right.append(last_left)
#             right_to_left.append(last_right)
#     right_to_left = list(reversed(right_to_left))
#     print(left_to_right)
#     print(right_to_left)
#     cnt = 0
#     for i in range(n):
#         if i == 0:
#             pre_num = 0
#         else: 
#             pre_num = left_to_right[i -1]
#         if i == n - 1:
#             post_num = 0
#         else:
#             post_num = right_to_left[i + 1]
#         print(f'i : {i}, pre : {pre_num} , post, {post_num}')
#         if pre_num + (-1)**(n ) *post_num ==0:
#             print(f'fair: i : {i}')
#             cnt+=1

#     return cnt


# if __name__ == '__main__':
#     target_list = [4,1,1,2,5,1,5,4]
#     print(fair(target_list))
        
# @lc code=end

