/*
 * @lc app=leetcode id=278 lang=cpp
 *
 * [278] First Bad Version
 */

// @lc code=start
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        if(isBadVersion(0)){
            return 0;
        }
        if(!isBadVersion(n)){
            return -1;
        }
        int first_possible_bad = 0;
        int first_bad = n;
        while(first_possible_bad < first_bad){
            int mid = first_possible_bad + (first_bad - first_possible_bad) /2;
            if(!isBadVersion(mid)){
                first_possible_bad = mid  + 1;
            }
            else{
                first_bad = mid;
            }
        }
        if(isBadVersion(first_possible_bad)){
            return first_possible_bad;
        }
        return first_bad;
        
    }
};
// @lc code=end

