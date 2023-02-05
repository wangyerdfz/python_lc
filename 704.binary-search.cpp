/*
 * @lc app=leetcode id=704 lang=cpp
 *
 * [704] Binary Search
 */

// @lc code=start
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n == 0){
            return -1;
        }
        if ( n == 1){
            if(nums[0] == target){
                return 0;
            } 
            return -1;
        }
        int low = 0;
        int high = n -1;
        while( low < high){
            int mid = low + (high - low) / 2;
            if (nums[mid] == target){
                return mid;
            } 
            else if(nums[mid] < target){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        if( high == low && nums[low] == target){
            return low;
        }
        return -1;
    }
};
// @lc code=end

