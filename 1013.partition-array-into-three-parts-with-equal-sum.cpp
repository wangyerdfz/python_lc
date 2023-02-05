/*
 * @lc app=leetcode id=1013 lang=cpp
 *
 * [1013] Partition Array Into Three Parts With Equal Sum
 */

// @lc code=start
class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int n = arr.size();
        if (n == 0){
            return true;
        }
        if (n < 3){
            return false;
        }
        int sum_ = 0;
        for(int i : arr){
            sum_ += i;
        }
        if (sum_%3 != 0){
            return false;
        }
        int target = sum_ / 3;
        int tmp_sum = 0;
        int parts = 0;
        for(int i = 0; i < n; ++i){
            tmp_sum += arr[i];
            if (tmp_sum == target){
                parts++;
                tmp_sum = 0;
            }
        }
        return parts >= 3;
    }
};
// @lc code=end

