/*
 * @lc app=leetcode id=509 lang=cpp
 *
 * [509] Fibonacci Number
 */

// @lc code=start
class Solution {
public:
    int fib(int n) {
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 1;
        }
        unsigned long arr[3];
        arr[0] = 0;
        arr[1] = 1;
        int i = 2;
        for( i = 2; i< n; ++i){
            arr[i % 3] = arr[(i -1) % 3] + arr[(i - 2)%3];
        }
        return(arr[(i -1) % 3] + arr[(i - 2)%3]);
        

    }
};
// @lc code=end

