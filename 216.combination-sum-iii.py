#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def comb_helper(k, sum_, start):
            
            res = []
            if k == 1:
                if sum_ >= start and sum_ <= 9:
                    return [[sum_]]
                return res

            if k > (9 - start + 1):
                return res
            sum_min = 0
            for i in range(k):
                sum_min += start + i
            sum_max = 0
            for i in range(k):
                sum_max += 9 - i
            if sum_ < sum_min or sum_ > sum_max:
                return res
            for i in range(start, 10):
                next_comb = comb_helper(k-1, sum_-i, i+1)
                if len(next_comb) > 0:
                    res += [[i] + x for x in next_comb]
            
            return res
        return comb_helper(k, n, 1)
            

# @lc code=end

