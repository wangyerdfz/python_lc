/*
 * @lc app=leetcode id=134 lang=cpp
 *
 * [134] Gas Station
 */

// @lc code=start
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int sum_gas = 0;
        int sum_cost = 0;
        for (int gas_num : gas){
            sum_gas += gas_num;
        }
        for(int cost_num : cost){
            sum_cost += cost_num;
        }
        if (sum_cost > sum_gas){ // wont make it
            return -1;
        }
        // will make it
        int n = gas.size();
        if (n == 1){
            return 0;
        }
        int min_val = INT_MAX;
        int min_idx = -1;
        int cur_val = 0;
        for(int i = 1; i <= n; ++i){
            cur_val += gas[(i - 1)%n] - cost[(i - 1)%n];
            if (cur_val < min_val){
                min_idx = i%n;
                min_val = cur_val;
            }
        }
        return min_idx;
    }
};
// @lc code=end

