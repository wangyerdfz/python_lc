#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 0:
            return []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        res = [[]]
        for num in counter:
            new_res = []
            for res_item in res:
                new_res += [res_item + [num]*i for i in range(counter[num]+1)]
            res = new_res
        
        return res
            

        # this basically s
        
# @lc code=end

