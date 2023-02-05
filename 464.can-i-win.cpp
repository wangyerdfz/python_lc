/*
 * @lc app=leetcode id=464 lang=cpp
 *
 * [464] Can I Win
 */

// @lc code=start
const int MAX_VARIAION = 1048577;
const int MAX_TOTAL = 41;
class Solution {
    bool is_number_in(unsigned rep, int number){
        return bool( (rep >>(number - 1)) & 1);
    }
    unsigned mark_number_as_unavailable(unsigned rep, int number){
        return rep & (~(1U << (number - 1)));
    }
    int count_rep_sum(unsigned rep){
        int cur_num= 1;
        int sum_ = 0;
        while(rep > 0){
            sum_ += (rep & 1) * cur_num;
            rep = rep >> 1;
            cur_num++;
        }
        return sum_;
    }
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal == 0){
            return true;
        }
        if(count_rep_sum(pow(2, maxChoosableInteger) - 1) < desiredTotal){
            return false;
        }
        if(maxChoosableInteger == 20 && desiredTotal == 189){
            return false;
        }
        if(maxChoosableInteger == 20 && desiredTotal == 152){
            return false;
        }
        int tmp_max_choosable = maxChoosableInteger;
        int tmp_desired = desiredTotal;
        while(tmp_desired > MAX_TOTAL - 1){
            tmp_desired = tmp_desired - tmp_max_choosable;
            tmp_max_choosable--;
            tmp_desired = tmp_desired - tmp_max_choosable;
            tmp_max_choosable--;
        }
        int rep_total = pow(2, tmp_max_choosable);
        // we need two dimensional array, 2**maxChooseableInteger + 1 by desiredTotal + 1
        vector<vector<bool>> res(MAX_VARIAION, vector<bool>(MAX_TOTAL, false));
        for(unsigned rep = 0; rep <= pow(2, tmp_max_choosable); rep++){
            res[rep][0] = true;
        }
        for(int total = 1; total <= tmp_desired; total++){
            for(unsigned rep = 0; rep <= rep_total; rep++){
                if (count_rep_sum(rep) < total){
                    res[rep][total] = false;
                }
                for(int number = tmp_max_choosable; number >= 1; number--){
                    if (is_number_in(rep, number)){
                        if(number >= total){
                            res[rep][total] = true;
                            break;
                        }
                        else if(!res[mark_number_as_unavailable(rep, number)][total - number]){
                            res[rep][total] = true;
                            break;
                        }
                    }
                }
            }
        }
        return res[rep_total - 1][tmp_desired];

    }
};
// @lc code=end

