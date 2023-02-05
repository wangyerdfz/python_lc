#
# @lc app=leetcode id=1414 lang=python3
#
# [1414] Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
#

# @lc code=start
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # if k < 2: return k
        # a, b = 1, 1
        # while b <= k:
        #     a, b = b, a + b
        # return self.findMinFibonacciNumbers(k - a) + 1
        if k == 1:
            return 1
        if k == 2:
            return 1
        low = 1
        high = 2
        sum_ = low + high
        while(sum_ < k):
            low = high
            high = sum_
            sum_ = low + high
        if sum_ == k:
            return 1
        return self.findMinFibonacciNumbers(k - high) + 1
        # result_list = [-1]* (k + 1)
        # low = 1
        # high = 2
        # sum_ = low + high
        # result_list[1] = 1
        # result_list[2] = 1
        # while(sum_ <= k):
        #     result_list[sum_] = 1
        #     low = high
        #     high = sum_
        #     sum_ = low + high
        # prev_feb = 1
        # for i in range(1, k + 1):
        #     if result_list[i] == 1:
        #         prev_feb = i
        #         continue

        #     result_list[i] = result_list[i - prev_feb] + 1
        # return result_list[k]

def print_first_fibo(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    
    result_list = [-1]* (k + 1)
    low = 1
    high = 2
    sum_ = low + high
    result_list[1] = 1
    result_list[2] = 1
    while(sum_ <= k):
        result_list[sum_] = 1
        low = high
        high = sum_
        sum_ = low + high
        
    prev_feb = 1
    for i in range(1, k + 1):
        if result_list[i] == 1:
            prev_feb = i
            continue
        result_list[i] = result_list[i - prev_feb] + 1
    return result_list[k]

if __name__ == '__main__':
    print_first_fibo(10000)
        
# @lc code=end

