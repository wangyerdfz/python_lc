#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(i : int):
            prod_ = 1
            while(i > 1):
                prod_ *= i
                i -= 1
            return int(prod_)
        if n == 1:
            return "1"
        res = ""
        target = k - 1
        num_of_cat = factorial(n)
        selections = list(range(1, n+1))
        while(selections):
            num_of_cat = num_of_cat // (n)
            
            num_ = selections.pop(target // num_of_cat)
            res += str(num_)
            target = target % num_of_cat
            n -= 1

        return res



# @lc code=end

