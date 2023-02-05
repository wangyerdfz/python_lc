/*
 * @lc app=leetcode id=2169 lang=cpp
 *
 * [2169] Count Operations to Obtain Zero
 */

// @lc code=start
class Solution {
public:
    int countOperations(int num1, int num2) {
        int num_op = 0;
        if(num1 < 0 || num2 < 0){
            return -1;
        }
        while(num1 && num2){
            if(num1  == num2){
                return num_op + 1;
            }
            if(num1 < num2){
                num2 = num2 - num1;
                num_op++;
            }
            else{
                num1 = num1 - num2;
                num_op++;
            }
        }
        return num_op;
    }
};
// @lc code=end

