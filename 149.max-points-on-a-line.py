#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        def cal_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:
                return float('inf')
            return (y2-y1)/(x2-x1)


        max_ = 0

        for idx, p1 in enumerate(points):
            slope_cnt = defaultdict(int)
            for p2 in points[idx+1:]:
                slope = cal_slope(p1, p2)
                slope_cnt[slope] += 1
                max_ = max(slope_cnt[slope], max_)

        return max_ + 1

# @lc code=end

