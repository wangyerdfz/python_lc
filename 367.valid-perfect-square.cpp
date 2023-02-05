/*
 * @lc app=leetcode id=367 lang=cpp
 *
 * [367] Valid Perfect Square
 */

// @lc code=start
class Solution {
public:
    bool isPerfectSquare(int num) {
        // binary search
        if(num <= 1){
            return true;
        }
        int low = 1;
        int high = num;
        while( low < high){
            int mid = low + (high - low)/2;
            if (num % mid == 0 && num / mid == mid){
                return true;
            }
            if ((num % mid == 0 && num/mid > mid) || (num % mid != 0 && num / mid >= mid)){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        return false;
    }
};
// @lc code=end

