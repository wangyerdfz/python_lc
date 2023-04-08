#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    # def __init__(self):
    #     self.cache = {}
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex-1)
        return [x + y for x, y in zip([0] + prev_row, prev_row + [0])]
        
# @lc code=end

