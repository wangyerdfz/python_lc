/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        if (n == 0){
            return 0;
        }
        int start = 0;
        int end = n -1;
        while(true){
            // search from front : first val 
            while(start < n){
                if (nums[start] == val){
                    break;
                }
                start++;
            }
            while(end > 0){
                if (nums[end] != val){
                    break;
                }
                end--;
            }
            if (start < end){
                int tmp = nums[start];
                nums[start]= nums[end];
                nums[end] = tmp;
            }
            else{
                break;
            }
        }
        int res = 0;
        while(res < n){
            if (nums[res] == val){
                return res;
            }
            res+=1;
        }
        return res;
    }
};
// @lc code=end

