#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            count_ = counter.get(i, 0)
            if count_ != 2:
                counter[i] = count_+1
            else:
                counter.pop(i)
        return list(counter.keys())[0]
# @lc code=end

