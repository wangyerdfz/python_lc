#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start

# SYMBOL_LIST = ['I', 'IV', 'V', 'IX', 'X', 
#                 'XL', 'L', 'XC', 'C', 'CD', 
#                 'D', 'CM', 'M']
# NUMBER_LIST = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]



SYMBOL_LIST = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

NUMBER_LIST = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]





class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""
        for sym, num_ in zip(reversed(SYMBOL_LIST), reversed(NUMBER_LIST)):
            if num >= num_:
                return sym + self.intToRoman(num - num_)
        return ""




        # if num == 0:
        #     return ""
        # for i, p in zip(reversed(NUMBER_LIST), reversed(SYMBOL_LIST)):
        #     if i <= num:
        #         return p + self.intToRoman(num - i)
        # return ""


        
        
# @lc code=end

