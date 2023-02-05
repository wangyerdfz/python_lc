/*
 * @lc app=leetcode id=877 lang=cpp
 *
 * [877] Stone Game
 */

// @lc code=start
class Solution {
    bool stoneGame_helper(vector<int>& piles, int left, int right, int required_to_win){
        if (right < left){
            return required_to_win <0;
        }
        if(left == right){
            return piles[left] > required_to_win;
        }
        bool take_left = stoneGame_helper(piles, left + 1, right, -(required_to_win - piles[left]));
        bool take_right = stoneGame_helper(piles, left, right - 1, -(required_to_win - piles[right]));
        return (!take_left) || (!take_right);
        
    }
public:
    bool stoneGame(vector<int>& piles) {
        // int n = piles.size();
        // if(n == 0){
        //     return true;
        // }
        // if( n == 1){
        //     return piles[0] > 0;
        // }
        // return stoneGame_helper(piles, 0, n - 1, 0);
        return true;
    }
};
// @lc code=end

