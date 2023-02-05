#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        num_list = []
        while( x > 0):
            num_list.append(x%10)
            x = x // 10
        while num_list:
            if len(num_list) <= 1:
                return True
            if num_list[-1] != num_list[0]:
                return False
            num_list.pop(0)
            num_list.pop()

        return True
            

        # if x < 0:
        #     return False
        # if x == 0:
        #     return True
        # digit_list = []
        # while(x > 0):
        #     digit_list.append(x % 10)
        #     x = x // 10
        # i = 0
        # j = len(digit_list) - 1
        # while(i <= j):
        #     if digit_list[i] != digit_list[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True
# @lc code=end

