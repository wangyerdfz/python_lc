#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import numpy as np
        p_list = []
        idx = 0
        while idx < len(p):
            if (idx < len(p)-1) and (p[idx + 1] == '*'):
                p_list.append(p[idx:idx+2])
                idx += 2
            else:
                p_list.append(p[idx])
                idx+=1

        ## make the full array
        res_array = False * np.full((len(p_list) + 1, len(s) + 1), False)
        res_array[-1, -1] = True
        for idx in range(len(s)): #  boundary condition 1, with p = "", any non empty string s would be no match
            res_array[-1, idx] = False 
        for idx in range(len(p_list)-1, -1, -1):  # boundary condition 2, when s = "" only when p has  a series of ".*" or "a*" would the value be True. otherwise False
            if len(p_list[idx]) == 1:
                res_array[idx, -1] = False
            else:
                res_array[idx, -1] = res_array[idx+1, -1] 

        for p_idx in range(len(p_list)-1, -1, -1):
            if len(p_list[p_idx]) == 2: # .* or letter*
                if p_list[p_idx][0] == '.':
                    for s_idx in range(len(s) -1, -1, -1):
                        res_array[p_idx, s_idx] = res_array[p_idx + 1, s_idx ] or res_array[p_idx , s_idx + 1]
                else:
                    for s_idx in range(len(s) -1, -1, -1):
                        res_array[p_idx, s_idx] = (res_array[p_idx + 1, s_idx] ) or (s[s_idx] == p_list[p_idx][0] and res_array[p_idx, s_idx + 1])
            else: # single letter or a dot
                if p_list[p_idx] == '.':
                    for s_idx in range(len(s) -1, -1, -1):
                        res_array[p_idx, s_idx] = res_array[p_idx+1, s_idx+1]
                else: # single letter
                    for s_idx in range(len(s) -1, -1, -1):
                        res_array[p_idx, s_idx] = (res_array[p_idx+1, s_idx+1]) and (s[s_idx] == p_list[p_idx])



        return res_array[0, 0]



    


        


        
        
# @lc code=end

