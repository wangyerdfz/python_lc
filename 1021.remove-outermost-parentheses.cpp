/*
 * @lc app=leetcode id=1021 lang=cpp
 *
 * [1021] Remove Outermost Parentheses
 */

// @lc code=start
class Solution {
public:
    string removeOuterParentheses(string s) {
        string res = "";
        int n = s.size();
        if (n == 0){
            return res;
        }
        int diff = 0;
        for( char c : s){
            if (c == '('){
                if(diff > 0){
                    res += c;
                }
                diff++;
            }
            if ( c == ')'){
                diff--;
                if(diff > 0){
                    res += c;
                }
            }
        }
        return res;
    }
};
// @lc code=end

