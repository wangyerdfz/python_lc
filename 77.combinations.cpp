/*
 * @lc app=leetcode id=77 lang=cpp
 *
 * [77] Combinations
 */

// @lc code=start

vector<vector<int>> combine_helper(int n, int k){
    vector<vector<int>> res;
    if (k == 0){
        vector<int> temp;
        res.push_back(temp);
        return res;
    }
    vector<vector<int>> start = combine_helper(n, k - 1);
    

}

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        
    }
};
// @lc code=end

