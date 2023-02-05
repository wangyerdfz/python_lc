/*
 * @lc app=leetcode id=709 lang=cpp
 *
 * [709] To Lower Case
 */

// @lc code=start
class Solution {
public:
    string toLowerCase(string s) {
        string res = "";
        for(char c : s){
            if( c >= 'A' && c <= 'Z'){
                res += (c - 'A' + 'a');
            }
            else{
                res += c;
            }
        }
        return res;
    }
};
// @lc code=end

