/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2){
            return nums[0];
        }
        unordered_map<int, int> count;
        for(int i = 0; i < n; ++i){
            if(count.find(nums[i]) == count.end()){
                count[nums[i]] = 1;
            }
            else{
                count[nums[i]] = count[nums[i]] + 1;
                if (count[nums[i]] >= (n + 1) /2){
                    return nums[i];
                }
            }

        }
        return -1;
    }
};
// @lc code=end

