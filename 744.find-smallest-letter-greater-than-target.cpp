/*
 * @lc app=leetcode id=744 lang=cpp
 *
 * [744] Find Smallest Letter Greater Than Target
 */

// @lc code=start
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int n = letters.size();
        if(letters[0] > target){
            return letters[0];
        }
        if(letters[n - 1] <= target){
            return letters[0];
        }
        int low = 0;
        int high = n - 1;
        while( low < high){
            int mid = low + (high - low) /2;
            if(letters[mid] <= target){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
        return letters[low];
    }
};
// @lc code=end

