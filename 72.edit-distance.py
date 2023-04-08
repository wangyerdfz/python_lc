#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)
        if n1 == 0 or n2 == 0:
            return abs(n1- n2)
        
        import numpy as np
        
        answer_mat = -1*np.ones((n1+1, n2+1), dtype=int)
        for i in range(n1 + 1):
            answer_mat[i, n2] = n1 - i
        for i in range(n2 + 1):
            answer_mat[n1, i] = n2 - i
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[j]:
                    answer_mat[i, j] = answer_mat[i+1, j+1]
                else:
                    insert_step = 1 + answer_mat[i, j+1]
                    deletion_step = 1 + answer_mat[i+1, j]
                    swap_step = 1 + answer_mat[i+1, j+1]
                    answer_mat[i, j] =  min(insert_step, deletion_step, swap_step)


        return answer_mat[0, 0]

        # if word1[0] == word2[0]:
        #     return self.minDistance(word1[1:], word2[1:])

        # # insert word2[0] at word1:
        # insert_step = 1 + self.minDistance(word1, word2[1:])
        # deletion_step = 1 + self.minDistance(word1[1:], word2)
        # swap_step = 1 + self.minDistance(word1[1:], word2[1:])
        # return min(insert_step, deletion_step, swap_step)

# @lc code=end

