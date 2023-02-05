/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> pos_dict;
        int max = 0;
        int n = s.size();
        if (n <= 0){
            return 0;
        }
        int prev = -1;
        for (int i = 0; i < n; ++i){
            if (pos_dict.find(s[i]) != pos_dict.end()){
                if (prev < pos_dict[s[i]] ){
                    prev = pos_dict[s[i]];
                    pos_dict[s[i]]  = i;
                }
            }
            if (max < i - prev){
                max = i - prev;
            }
            pos_dict[s[i]] = i;
        }
        return max;
    }
};
// @lc code=end

