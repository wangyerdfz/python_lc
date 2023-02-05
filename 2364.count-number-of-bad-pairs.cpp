/*
 * @lc app=leetcode id=2364 lang=cpp
 *
 * [2364] Count Number of Bad Pairs
 */

// @lc code=start
class Solution {
    vector<int> parent;
public:
    long long countBadPairs(vector<int>& nums) {
        // union find
        int n = nums.size();
        if( n <= 1){
            return 0;
        }
        unordered_map<int, int> count;
        long long sum_ = 0;
        for(int i = 0; i < n; ++i){
            if(count.find(nums[i] - i) == count.end()){
                sum_ += i;
                count[nums[i] - i] = 1;
            }
            else{
                sum_ += i - count[nums[i] - i];
                count[nums[i] - i] = count[nums[i] - i] + 1;
            }
        }
        return sum_;

    }
};
// @lc code=end

