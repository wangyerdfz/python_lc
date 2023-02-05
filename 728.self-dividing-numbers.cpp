/*
 * @lc app=leetcode id=728 lang=cpp
 *
 * [728] Self Dividing Numbers
 */

// @lc code=start
class Solution {
public:
    bool is_self_dividing( int num){
        if (num <= 0){
            return false;
        }
        int tmp_num = num;
        while(num >0){
            int dig = num%10;
            if (dig == 0){
                return false;
            }
            if ( tmp_num % dig != 0){
                return false;
            }
            num = num / 10;
        }
        return true;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        if (left > right){
            return {};
        }
        vector<int> res;
        for(int i = left; i <= right; ++i){
            if(is_self_dividing(i)){
                res.push_back(i);
            }
        }
        return res;
    }
};
// @lc code=end

