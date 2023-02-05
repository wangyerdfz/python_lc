#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num_ = 40
        while(num_ >= 40):
            a = rand7()
            b = rand7()
            num_ = (a-1)*7 + (b-1)
        return num_%10 + 1         
# @lc code=end

