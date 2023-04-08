#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        import numpy as np
        # define res[i, j, k]  as whether s1[:i] and s2[:j], s3[:i+j] can be interleaved. if k = 0 it means s1 goes first, or vice versa
        res = np.zeros((n1+1, n2+1, 2), dtype = bool) 
        # boundary condition
        res[0, 0, 0] = True
        for i in range(1, n1+1):
            res[i, 0, 0] = (s1[:i] == s3[:i])
        for i in range(1, n2+1):
            res[0, i, 0] = False
        res[0, 0, 1] = True
        for i in range(1, n2+1):
            res[0, i, 1] = s2[:i] == s3[:i]
        for i in range(1, n1+1):
            res[i, 0, 1] = False
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # calc res[i, j, 0] first res[i, j, 0] = True if exist k < i s.t. res[k, j, 1] = True and s1[k:i] == s3[j+k:j+i]
                tmp_ans = False
                for k in range(i):
                    if res[k, j, 1] and (s1[k:i] == s3[k+j:i+j]):
                        tmp_ans = True
                        break
                res[i, j, 0] = tmp_ans
                # calc res[i, j, 1].  res[i, j, 1] = True if exist k < j s.t. res[i, k, 0] = True and s2[k:j] == s3[i+k:i+j]
                tmp_ans = False
                for k in range(j):
                    if res[i, k, 0] and (s2[k:j] == s3[i+k:i+j]):
                        tmp_ans = True
                        break
                res[i, j, 1] = tmp_ans

        return res[n1, n2, 1] or res[n1, n2, 0]

                

        # def is_interleave_helper(s1, s2, s3):
        #     n1 = len(s1)
        #     n2 = len(s2)
        #     n3 = len(s3)
        #     if n1 + n2 != n3:
        #         return False
        #     if n2 == 0 and s1 == s3:
        #         return True
        #     if n1 == 0:
        #         return False
        #     ans = False
        #     for i in range(1,n1+1):
        #         ans = ans or (s1[:i] == s3[:i] and is_interleave_helper(s2, s1[i:], s3[i:]))
        #     return ans
        
        # return is_interleave_helper(s1, s2, s3) or is_interleave_helper(s2, s1, s3)

        

# @lc code=end

