/*
 * @lc app=leetcode id=941 lang=cpp
 *
 * [941] Valid Mountain Array
 */

// @lc code=start
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        if (n < 3){
            return false;
        }
        int left = 0;
        int right = n - 1;
        while(left  < n - 1 && arr[left] < arr[left + 1]){
            left++;
        }
        if(left == n - 1){
            return false;
        }
        while(right > 0 && arr[right] < arr[right - 1]){
            right--;
        }
        if(right == 0){
            return false;
        }
        return left >= right;
    }
};
// @lc code=end

