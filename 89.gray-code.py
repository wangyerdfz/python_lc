#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n <= 0:
            return []
        if n == 1:
            return [0, 1]
        tmp_list = self.grayCode(n-1)
        return tmp_list.copy() + [x + 2**(n-1) for x in reversed(tmp_list)]
        
# @lc code=end

