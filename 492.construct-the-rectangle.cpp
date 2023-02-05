/*
 * @lc app=leetcode id=492 lang=cpp
 *
 * [492] Construct the Rectangle
 */

// @lc code=start
class Solution {
public:
    vector<int> constructRectangle(int area) {
        if ( area == 0){
            return {0, 0};
        }
        if ( area == 1){
            return {1 ,1};
        }
        int last_l = -1;
        int last_w = -1;
        for(int w = 1; w * w <= area; ++w){
            if (area % w == 0){
                last_l = area/w;
                last_w = w;
            }
        }
        return {last_l, last_w};
    }
};
// @lc code=end

