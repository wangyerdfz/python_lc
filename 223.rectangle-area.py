#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        most_bottom = min(ay1, by1)
        most_top = max(ay2, by2)
        intersect_ver = max(0, ay2 - ay1 + by2 - by1 - (most_top - most_bottom))
        most_left = min(ax1, bx1)
        most_right = max(ax2, bx2)
        intersect_hor = max(0, ax2 - ax1 + bx2 - bx1 - (most_right - most_left))
        return (ay2 - ay1)*(ax2 - ax1) + (by2 - by1) * (bx2 - bx1) - intersect_hor*intersect_ver
# @lc code=end

