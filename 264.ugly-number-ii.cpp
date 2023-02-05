/*
 * @lc app=leetcode id=264 lang=cpp
 *
 * [264] Ugly Number II
 */

// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
        if (n <= 6){
            return n;
        }
        
        // unordered_map<int, int> pos;
        vector<int> ug_num(n, -1);
        ug_num[0] = 1;
        int t2 = 0, t3 = 0, t5 = 0;
        for(int i =1 ;i < n; ++i){
            int new_num = min(ug_num[t2] * 2, min(ug_num[t3] * 3, ug_num[t5] * 5));
            if(new_num == ug_num[t2] * 2){
                t2++;
            }
            if(new_num == ug_num[t3] * 3){
                t3++;
            }
            if(new_num == ug_num[t5] * 5){
                t5++;
            }
            ug_num[i] = new_num;
        }
        return ug_num[n - 1];
    }
};
// @lc code=end

