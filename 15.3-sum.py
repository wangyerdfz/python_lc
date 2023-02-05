#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        res = []

        if n <=2:
            return res

        pos_dict = {}
        for idx, i in enumerate(nums):
                pos_dict[i] = idx

        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if nums[i] + 2*nums[j] > 0:
                    continue
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                if -nums[i]-nums[j] in pos_dict:
                    if pos_dict[-nums[i]-nums[j]] > j:
                        res.append([nums[i], nums[j], -nums[i]-nums[j]])

        return res

            
        

        # res = []
        # nums.sort()

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]:
        #         continue
        #     left, right = i + 1, len(nums) - 1
        #     while(left < right):
        #         three_sum = a + nums[left] + nums[right]
        #         if three_sum > 0:
        #             right -= 1
        #         elif three_sum < 0:
        #             left += 1
        #         else:
        #             res.append([a, nums[left], nums[right]])
        #             left += 1
        #             while(nums[left] == nums[left - 1] and left < right):
        #                 left += 1
        
        # return res
        # def bin_search(list_in : list, target : int) -> bool:
        #     n_bin = len(list_in)
        #     if n_bin == 0:
        #         return False
        #     if n_bin == 1:
        #         return list_in[0] == target
        #     low = 0
        #     high = n_bin - 1
        #     while (low < high):
        #         mid = low + (high - low) // 2
        #         if list_in[mid] == target:
        #             return True
        #         if list_in[mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid
        #     return list_in[low] == target


        # ret_list = []
        # nums = list(nums)
        # n = len(nums)
        # if n <= 2:
        #     return ret_list
        # nums.sort()
        # for i in range(n):
        #     if nums[i] > 0:
        #         break
        #     for j in range(i + 1, n):
        #         if nums[i] + 2 * nums[j] > 0:
        #             break
        #         if bin_search( nums[j + 1: n], - nums[i] - nums[j]):
        #             ret_list.append([nums[i], nums[j], - nums[i] - nums[j]])

        # tmp_list = []
        # for list_iter in ret_list:
        #     if list_iter not in tmp_list:
        #         tmp_list.append(list_iter)
        # return tmp_list
# @lc code=end



