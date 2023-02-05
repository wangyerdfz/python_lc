/*
 * @lc app=leetcode id=344 lang=cpp
 *
 * [344] Reverse String
 */

// @lc code=start
class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        if(n <= 1){
            return ;
        }
        char tmp;
        for(int i = 0; n - 1 - i > i; ++i){
            tmp = s[i];
            s[i] = s[n - 1 - i];
            s[n - 1 - i] = tmp;
        }
        return;

    }
};
// @lc code=end

