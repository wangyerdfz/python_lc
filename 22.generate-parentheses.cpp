/*
 * @lc app=leetcode id=22 lang=cpp
 *
 * [22] Generate Parentheses
 */

// @lc code=start



vector<string> generate_par_helper(int left, int right){
    vector<string> res;
    if (left == 0){
        string s(right, ')');
        res.push_back(s);
        return res;
    }
    if (left == right){
        vector<string> next_list = generate_par_helper(left - 1, right);
        for (int i = 0; i < next_list.size(); ++i){
            res.push_back("(" + next_list[i]);
        }
    }
    else{
        vector<string> next_list_1 = generate_par_helper(left -1, right);
        vector<string> next_list_2 = generate_par_helper(left, right - 1);
        for (int i = 0; i < next_list_1.size(); ++i){
            res.push_back("(" + next_list_1[i]);
        }
        for (int i = 0; i < next_list_2.size(); ++i){
            res.push_back(")" + next_list_2[i]);
        }
    }
    return res;
}
class Solution {
public:
    vector<string> generateParenthesis(int n) {


        if (n ==0){
            return {};
        }
        return generate_par_helper(n, n);
    }
};
// @lc code=end

