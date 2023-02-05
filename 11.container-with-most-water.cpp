/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        if (n <= 1){
            return 0;
        }
        int left = 0;
        int right = n - 1;
        int max_ = 0;
        while(left < right){
            int cur_water = min(height[left], height[right]) * (right - left);
            if (cur_water > max_){
                max_ = cur_water;
            }
            if (height[left] > height[right]){
                right -= 1;
            }
            else{
                left += 1;
            }
        }
        return max_;
    }
};
// @lc code=end

