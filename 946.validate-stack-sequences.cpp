/*
 * @lc app=leetcode id=946 lang=cpp
 *
 * [946] Validate Stack Sequences
 */

// @lc code=start
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        vector<int> stack;
        int n_push = pushed.size();
        int n_pop = popped.size();
        if (n_push  != n_pop){
            return false;
        }
        int pop_i = 0;
        for (auto val : pushed){
            stack.push_back(val);
            while(!stack.empty() && stack.back() == popped[pop_i]){
                pop_i++;
                stack.pop_back();
            }
        }
        return stack.empty();
        // int push_i = 0;
        // int pop_i = 0;
        // while(push_i < n_push && pop_i < n_pop){
        //     if(stack.size == 0){
        //         stack.push_back(pushed[push_i]);
        //         push_i++;
        //     }
        //     else{
        //         int n = stack.size();
        //         if (stack[n - 1] == popped[pop_i]){
        //             stack.pop_back();
        //             pop_i++;
        //         }
        //         else{
        //             stack.push_back(pushed[push_i]);
        //             push_i++;
        //         }
        //     }
        // }
    }
};
// @lc code=end

