/*
 * @lc app=leetcode id=279 lang=cpp
 *
 * [279] Perfect Squares
 */

// @lc code=start
class Solution {
public:
    int numSquares(int n) {
        if (n == 0){
            return 1;
        }
        vector<int> res(n + 1, INT_MAX);
        res[0] = 0;
        int count = 1;
        while( count * count <= n){
            int sq = count * count;
            for (int i = sq; i < n + 1; ++i){
                res[i] = min(res[i - sq] + 1, res[i]);
            }
            count++;
        }


        return res[n];

    }
};
// @lc code=end

