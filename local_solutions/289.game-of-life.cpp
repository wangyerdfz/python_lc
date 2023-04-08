#include<iostream>
#include<vector>
using namespace std; 
 
 
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

void print_mat(vector<vector<int>> mat){
    int m = mat.size();
    int n = mat[0].size();
    for (int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j){
            cout << mat[i][j] << " "; 
        }
        cout << endl;
    }
}

void print_mat(int m, int n, vector<int> mat){
    for (int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j){
            cout << mat[i * m + j] << " "; 
        }
        cout << endl;
    }
}

int main(){
    vector<vector<int>> board{{0, 1, 0},{0, 0, 1},{1, 1, 1 },{0, 0, 0}};
    print_mat(board);
    vector<vector<int>> neib = count_neighbor(4, 3, board);
    print_mat(neib);


    return 1;
}