/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> h_table {};
        int n = nums.size();
        for(int i {0}; i < n; ++i){
            if( h_table.find(target - nums[i]) != h_table.end()){
                return {h_table[target - nums[i]], i};
            }
            h_table[nums[i]] = i;
        }
        return {-1, -1};


        // method 2 : hash table
        // unordered_map<int, int> dict;
        // int n = nums.size();
        // for (int i = 0; i < n; ++i){
        //     if (dict.find(target - nums[i]) != dict.end()){
        //         return { dict[target - nums[i]], i};
        //     }
        //     else{
        //         dict[nums[i]] = i;
        //     }
        // }
        // return {-1, -1};

        // method 1 brute force
        // int n = nums.size(); // use size
        // vector<int> answer;
        // for (int i = 0 ; i < n; ++i){
        //     for (int j = i + 1; j < n; ++j){
        //         if (nums[i] + nums[j] == target){
        //             answer.push_back(i);
        //             answer.push_back(j);
        //         } 
        //     }
        // }
        // return answer;
    }
};
// @lc code=end

