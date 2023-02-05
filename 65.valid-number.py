#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        def if_digits(s):
            n = len(s)
            if n == 0:
                return False

            for c in s:
                if c not in list("0123456789"):
                    return False
                
            return True
            
        def if_sign(s):
            n = len(s)
            if n <= 0 or n > 1:
                return False
            return s in list("+-")
        
        def if_integer(s):
            n = len(s)
            if n <= 0:
                return False
            start = 0
            if if_sign(s[0]):
                start += 1
            return if_digits(s[start:])
        
        def if_signless_decimal(s):
            n = len(s)
            if n <= 0:
                return False
            dot_pos = -1
            for i, c in enumerate(s):
                if c == '.':
                    dot_pos = i
                    break
            if dot_pos == -1:
                return False
            if dot_pos == 0:
                return if_digits(s[1:])
            if dot_pos == n-1:
                return if_digits(s[:n-1])
            return if_digits(s[:dot_pos]) and if_digits(s[dot_pos+1:])
        
        def if_decimal(s):
            n = len(s)
            if n <= 0:
                return False
            return ((s[0] in list("+-")) and if_signless_decimal(s[1:])) or if_signless_decimal(s)
        
        n = len(s)
        if s == 0:
            return False
        e_pos = -1
        for i, c in enumerate(s):
            if c in list("eE"):
                e_pos = i
                break

        return ((e_pos == -1) and (if_decimal(s) or if_integer(s))) or ((e_pos > -1) and (if_decimal(s[:e_pos]) or if_integer(s[:e_pos])) and (if_integer(s[e_pos + 1:])))
        

            
        


                


        # # 0 : is empty
        # # 1 : is only digits
        # # 2 : is decimal excluding only digits
        # # 3 : is integer excluding only digits, so it means there's an e or E of + or -
        # import numpy as np
        # n = len(s)
        # if n == 0:
        #     return False
        # res = np.zeros((4, n + 1), dtype=bool)
        # res[0, n] = True
        # res[1, n] = False
        # res[2, n] = False
        # res[3, n] = False
        # for i in range(n -1, -1, -1):
        #         if not (s[i] in ['e', 'E', '+', '-', '.'] or s[i].isnumeric()):
        #             return False
        #         if s[i].isnumeric(): # if its a digit, then they all stay the same
        #             if res[1, i+1]:
        #                 res[1, i] = True
        #                 continue
        #             if res[2, i+1]:
        #                 res[2, i] = True
        #                 continue
        #             if res[3, i+1]: # if its already
        #                 return False


        
        
# @lc code=end

