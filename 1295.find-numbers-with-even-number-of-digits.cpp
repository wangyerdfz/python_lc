/*
 * @lc app=leetcode id=1295 lang=cpp
 *
 * [1295] Find Numbers with Even Number of Digits
 */

// @lc code=start
class Solution {
    int if_even(int num){
        if(num / 100000 >=1){
            return 1;
        }
        if( num / 1000 >= 1 && num/1000 < 10){
            return 1;
        }
        if(num / 10 >= 1 && num / 10 < 10){
            return 1;
        }
        return 0;
    }
public:
    int findNumbers(vector<int>& nums) {
        int sum_ = 0;
        for(int num:nums){
            sum_ += if_even(num);
        }
        return sum_;
    }
    
};
// @lc code=end

