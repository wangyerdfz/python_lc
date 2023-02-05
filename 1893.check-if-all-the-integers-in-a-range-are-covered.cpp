/*
 * @lc app=leetcode id=1893 lang=cpp
 *
 * [1893] Check if All the Integers in a Range Are Covered
 */

// @lc code=start
class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        bool covered[51] = {false};
        for(auto range : ranges){
            for(int i = range[0]; i <= range[1]; ++i){
                covered[i] = true;
            }
        }
        for(int i = left; i <= right; ++i){
            if(!covered[i]){
                return false;
            }
        }
        return true;

    }
};
// @lc code=end

