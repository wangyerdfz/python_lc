#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for idx, c in enumerate(citations):
            if idx + 1 > c:
                return idx 

        return len(citations)
# @lc code=end

