/*
 * @lc app=leetcode id=836 lang=cpp
 *
 * [836] Rectangle Overlap
 */

// @lc code=start
class Solution {
    bool if_overlap(int x1_1, int x2_1, int x1_2, int x2_2){
        int max_x = max(x2_1, x2_2);
        int min_x = min(x1_1, x1_2);
        return ((max_x - min_x - (x2_1 - x1_1) - (x2_2 - x1_2)) < 0);
    }
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        bool overlap_x = if_overlap(rec1[0], rec1[2], rec2[0], rec2[2]);
        bool overlap_y = if_overlap(rec1[1], rec1[3], rec2[1], rec2[3]);
        return overlap_x && overlap_y;
    }
};
// @lc code=end

