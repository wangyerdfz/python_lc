/*
 * @lc app=leetcode id=860 lang=cpp
 *
 * [860] Lemonade Change
 */

// @lc code=start
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int num_of_five = 0;
        int num_of_ten = 0;
        int num_of_twenty = 0;
        for(int bill : bills){
            if ( bill == 5){
                num_of_five += 1;
            }
            if(bill == 10){
                if (num_of_five <= 0){
                    return false;
                }
                num_of_five -= 1;
                num_of_ten += 1;
            }
            if(bill == 20){
                // giving 10 and 5 is always a dominate strategy
                if( num_of_ten <= 0){
                    if (num_of_five <= 2){
                        return false;
                    }
                    num_of_five -= 3;
                    num_of_twenty += 1;
                }
                else{
                    if(num_of_five <= 0){
                        return false;
                    }
                    num_of_five -= 1;
                    num_of_ten -= 1;
                    num_of_twenty += 1;
                }
            }
        }
        return true;
    }
};
// @lc code=end

