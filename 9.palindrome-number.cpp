/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        if (x == 0){
            return true;
        }
        if (x < 0 || x %10 == 0){
            return false;
        }
        string s = to_string(x);
        int left = 0;
        int right = s.size() - 1;
        while(left <= right){
            if (s[left] != s[right]){
                return false;
            }
            left+=1;
            right-=1;
        }
        return true;
    }
};
// @lc code=end

