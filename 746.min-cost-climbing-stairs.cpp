/*
 * @lc app=leetcode id=746 lang=cpp
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> total_cost(n + 1, -1);
        total_cost[n - 1] = cost[n - 1];
        total_cost[n] = 0;
        for(int i = n - 2; i >= 0; --i){
            total_cost[i] = min( total_cost[i + 1], total_cost[i + 2]) + cost[i];
        }
        return min(total_cost[0], total_cost[1]);    
    }
};
// @lc code=end

