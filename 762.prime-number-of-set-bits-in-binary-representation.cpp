/*
 * @lc app=leetcode id=762 lang=cpp
 *
 * [762] Prime Number of Set Bits in Binary Representation
 */

// @lc code=start
class Solution {
    bool if_prime(int n){
        if (n == 2 || n == 3 || n == 5 || n == 7 || n == 11 || n == 13 || n == 17 || n == 19 || n == 23 || n == 29 || n == 31 || n == 37){
            return true;
        }
        return false;
    }
    int count_bits(int n){
        int count = 0;
        while(n > 0){
            count += n & 1;
            n = n >> 1;
        }
        return count;
    }
public:
    
    int countPrimeSetBits(int left, int right) {
        int count = 0;
        for(int i = left; i <= right; ++i){
            if ( if_prime(count_bits(i))){
                count++;
            }
        }
        return count;
    }
};
// @lc code=end

