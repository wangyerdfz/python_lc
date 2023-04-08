#include <iostream>
#include <vector>
using std::vector;
using std::endl;
using std::cout;
// int change_helper(int amount, vector<int>& coins, int start, int end){
//     cout << "called" << amount << start << end << endl;
//     if (amount <= 0){
//         return 0;
//     }
//     if ( start > end){
//         return 0;
//     }
//     if (start == end){
//         if (amount % coins[start] == 0){
//             return 1;
//         }
//         else{
//             return 0;
//         }
//     }
//     int sum_ = 0;
//     for(int i = start; i <= end; ++i){
//         if (amount == coins[i]){
//             sum_ += 1;
//         }
//         if (amount > coins[i]){
//             sum_ += change_helper(amount - coins[i], coins, i, end);
//         }
//     }
//     return sum_;
// }

// int change(int amount, vector<int>& coins) {
//     if (amount == 0){
//         return 0;
//     }
//     int n = coins.size();
//     if(n == 0){
//         return 0;
//     }
//     if(n == 1){
//         if (amount% coins[0] == 0){
//             return 1;
//         }
//         return 0;
//     }
//     return change_helper(amount, coins, 0, n - 1);
// }

int change(int amount, vector<int>& coins) {
    if (amount == 0){
        return 1;
    }
    vector<int> res(amount + 1, 0);
    // cout << "good til here" << endl;
    res[0] = 1;
    // cout << "good til here" << endl;
    
    for(int j = 0; j < coins.size(); ++j){
        for(int i = 1; i <= amount; ++i){
            // cout << "i = " << i << "j = " << j << endl;
            if ( i - coins[j] >= 0){
                res[i] += res[i - coins[j]];
            }
        }
    }
    for( int i = 0; i <= amount; ++i){
        cout << res[i] << endl;
    }
    return res[amount];
}

int main(){
    int amount = 5;
    vector<int> v{1,2,5};
    int ways = change(amount, v);
    cout << ways << endl;
    return 0;
}

// @lc code=end

