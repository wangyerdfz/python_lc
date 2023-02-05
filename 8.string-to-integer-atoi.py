#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
from lib2to3.pgen2.token import STAR
from re import L


class Solution:
    def myAtoi(self, s: str) -> int:
        res_num = 0
        neg = False
        DIGITS = '0123456789'
        SIGNS = '+-'
        STARTING_NUM = False
        EXIST_SIGN = False


        s = s.strip()
        if len(s) == 0:
            return 0
        
        for i in range(len(s)):
            if s[i] not in DIGITS + SIGNS:
                if STARTING_NUM == False:
                    return 0
                if STARTING_NUM == True:
                    break
            if s[i] in DIGITS + SIGNS:
                if s[i] == '+':
                    if STARTING_NUM :
                        break
                    if EXIST_SIGN :
                        return 0
                    EXIST_SIGN = True
                if s[i] == '-':
                    if STARTING_NUM :
                        break
                    if EXIST_SIGN :
                        return 0

                    EXIST_SIGN = True
                    neg = True
                if s[i] in DIGITS :
                    STARTING_NUM = True
                    res_num = res_num * 10 + int(s[i])
            
        if neg:
            res_num = res_num * -1
        if (res_num < -1 * 2**31):
            return -1 * 2**31
        if (res_num > 2**31 - 1):
            return 2**31 - 1
        return res_num

        
# @lc code=end

