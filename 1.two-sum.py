#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return []

        pos_dict = {}
        for idx, i in enumerate(nums):
            if target - i in pos_dict:
                return [idx, pos_dict[target - i]]
            pos_dict[i] = idx

        
        return []



        # n = len(nums)
        # if n <= 1:
        #     return []
        # val_dict = {}
        # for idx, i in enumerate(nums):
        #     if target - i in val_dict:
        #         return [idx , val_dict[target - i]]
        #     val_dict[i] = idx
        # return []




        # n = len(nums)
        # if n <= 1:
        #     return []
        # pos_dict = {}
        # for i, n in enumerate(nums):
        #     if target - n in pos_dict:
        #         return [pos_dict[target - n], i]
        #     pos_dict[n] = i
        
        # return []






        # pos_dict = {}
        # n = len(nums)
        # for i in range(n):
        #     j = pos_dict.get(target - nums[i], -1)
        #     if j >= 0:
        #         return [i , j]
        #     pos_dict[nums[i]] = i
        # return []



# interested in val in dict vs val in dict.keys()?
# from functools import wraps
# import time
# import random

# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         for _ in range(10000000):
#             result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__} Took {total_time:.4f} seconds')
#         return result
#     return timeit_wrapper

# @timeit
# def find_val_in_dict(num : dict, val : int) ->bool:
#     return val in num

# @timeit
# def find_val_in_dict_keys(num : dict, val : int) ->bool:
#     return val in num.keys()

# if __name__ == '__main__':
#     N = 1000000
#     val = random.randint(0, N - 1)
#     my_dict = {i : True for i in range(N)}
#     find_val_in_dict(my_dict, val)
#     find_val_in_dict_keys(my_dict, val)

# @lc code=end

