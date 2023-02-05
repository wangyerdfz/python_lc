#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for idx, c in enumerate(reversed(citations)):
            if idx + 1 > c:
                return idx
        return len(citations)
# @lc code=end

