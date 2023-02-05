#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        res = []
        intervals.sort(key=lambda x: x[0] * 10001 + x[1])
        res.append(intervals[0])
        for i in range(1, n):
            if intervals[i][0] > res[-1][1]: # no overlap
                res.append(intervals[i])
            else: # overlap
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res
# @lc code=end

