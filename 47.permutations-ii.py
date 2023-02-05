#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutation_helper( count_dict:dict):
            total_val = sum(count_dict.values())
            if total_val <= 0:
                return [[]]
            res = []
            for i in count_dict:
                if count_dict[i] > 0:
                    tmp_dict = count_dict.copy()
                    tmp_dict[i]-=1
                    res += [[i] + x for x in permutation_helper(tmp_dict)]
            
            return res


        n = len(nums)
        if n <= 0:
            return []

        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1

        return permutation_helper(my_dict)
        #     n = len(cand_list)
        #     if n <= 0:
        #         return [[]]
        #     res = []
        #     if count_dict.get(cand_list[0], 0) > 0:
        #         tmp_dict = count_dict.copy()
        #         tmp_dict[cand_list] -= 1
        #         res += [cand_list[0] + x for x in permutation_helper(cand_list, tmp_dict)]
        #     res += permutation_helper(cand_list[1:], count_dict.copy())
        #     return res


        # n = len(nums)
        # if n == 0:
        #     return []
        # count_dict = {}
        # for i in nums:
        #     count_dict[i] = count_dict.get(i, 0)
        # cand_list = list(count_dict.keys())
        # cand_list.sort()

        # return permutation_helper(cand_list, count_dict)



# @lc code=end

