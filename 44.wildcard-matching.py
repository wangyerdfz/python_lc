#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
import numpy as np
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_size = len(s)
        p_size = len(p)
        if(p_size == 0):
            return s_size == 0
        res = np.zeros((s_size + 1 , p_size + 1), dtype = bool)
        res[s_size, p_size] = True
        for i in range(s_size - 1):
            res[i, p_size] = False
        for i in range(p_size - 1, -1, -1):
            res[s_size, i] = (p[i] == '*') and (res[s_size, i + 1])
        for j in range(p_size - 1, -1 , -1):
            for i in range(s_size -1, -1, -1):
                if p[j].isalpha():
                    res[i, j] = (p[j] == s[i]) and (res[i + 1, j + 1])
                elif p[j] == '*':
                    res[i, j] = res[i + 1, j] or res[i, j + 1]
                else: # p[j] == ?
                    res[i, j] = res[i + 1, j + 1]
        return res[0, 0]

        
# @lc code=end

