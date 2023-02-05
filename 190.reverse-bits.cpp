/*
 * @lc app=leetcode id=190 lang=cpp
 *
 * [190] Reverse Bits
 */

// @lc code=start
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = (n & 0x1);
        for(int i = 1; i < 32; ++i){
            res = res << 1;
            res = res + ((n >> i) & 0x1);
        }
        return res;

    }
};
// @lc code=end

