/*
 * @lc app=leetcode id=1732 lang=cpp
 *
 * [1732] Find the Highest Altitude
 */

// @lc code=start
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int cur = 0;
        int highest = 0;
        for(int a : gain){
            cur += a;
            highest = max(highest, cur);
        }
        return highest;
    }
};
// @lc code=end

