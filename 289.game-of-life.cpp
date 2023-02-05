/*
 * @lc app=leetcode id=289 lang=cpp
 *
 * [289] Game of Life
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> count_neighbor(int m, int n, const vector<vector<int>> board){
            vector<vector<int>> res(m, vector<int>(n));
            for(int i = 0; i < m; ++i){
                for(int j = 0; j < n; ++j){
                    int sum_ = 0;
                    if (j == 0){
                        if (i == 0){
                            sum_ = board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1];
                        }
                        else if (i == m - 1){
                            sum_ = board[i - 1][j] + board[i][j + 1] + board[i - 1][j + 1];
                        }
                        else{
                            sum_ = board[i - 1][j] + board[i - 1][j + 1] + board[i][j + 1] + board[i + 1][j] + board[i + 1 ][j + 1];
                        }
                    }
                    else if (j == n -1){
                        if (i == 0){
                            sum_ = board[i + 1][j] + board[i][j - 1] + board[i + 1][j - 1];
                        }
                        else if (i == m - 1){
                            sum_ = board[i - 1][j] + board[i][j - 1] + board[i - 1][j - 1];
                        }
                        else{
                            sum_ = board[i - 1][j] + board[i - 1][j - 1] + board[i][j - 1] + board[i + 1][j] + board[i + 1 ][j - 1];
                        }
                    }
                    else{
                        if (i == 0){
                            sum_ = board[i][j - 1] + board[i][j + 1] + board[i + 1][j - 1] + board[i + 1][j] + board[i + 1 ][j + 1];
                        }
                        else if (i == m - 1){
                            sum_ = board[i][j - 1] + board[i][j + 1] + board[i - 1][j - 1] + board[i - 1][j] + board[i - 1 ][j + 1];
                        }
                        else{
                            sum_ = board[i][j - 1] + board[i][j + 1] + board[i - 1][j - 1] + board[i - 1][j] + board[i - 1 ][j + 1] + board[i + 1][j + 1] +  board[i + 1][j] +  board[i + 1][j - 1];
                        }
                    }
                    res[i][j] = sum_;
                }
            }
            return res;
        }

    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        if (m == 0){
            return ;
        }
        int n = board[0].size();
        if (n == 0){
            return;
        }

        vector<vector<int>> neib = count_neighbor(m, n, board);
        for(int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (board[i][j] == 1){
                    if ((neib[i][j] == 3) || (neib[i][j] == 2)){
                        board[i][j] = 1;
                    }
                    else{
                        board[i][j] = 0;
                    }
                }
                else{
                    if(neib[i][j] == 3){
                        board[i][j] = 1;
                    }
                    else{
                        board[i][i] = 0;
                    }
                }
            }
        }
        return ;

    }
};
// @lc code=end

