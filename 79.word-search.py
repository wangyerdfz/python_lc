#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m <= 0:
            return False
        n = len(board[0])
        if n <= 0:
            return False
        
        def exist_helper(board, word, i, j):
            if len(word) <= 0:
                return True
            if i < 0 or i >= m or j < 0 or j >=n or board[i][j] != word[0]:
                return False
            tmp = board[i][j] 
            board[i][j] = -1
            res = exist_helper(board, word[1:], i+1, j) or exist_helper(board, word[1:], i-1, j) or exist_helper(board, word[1:], i, j+1) or exist_helper(board, word[1:], i, j-1)
            board[i][j] = tmp
            return res
        

        for i in range(m):
            for j in range(n):
                if exist_helper(board, word, i, j):
                    return True
                
        return False




        # m = len(board)
        # if m <= 0:
        #     return False
        # n = len(board[0])
        # if n<=0:
        #     return False
        
        # def exist_helper(board, word, i, j):
        #     if len(word) <= 0:
        #         return True
        #     if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
        #         return False
        #     tmp = board[i][j]
        #     board[i][j] = -1
        #     res = False
        #     if exist_helper(board, word[1:], i+1, j) or exist_helper(board, word[1:], i-1, j) or exist_helper(board, word[1:], i, j+1) or exist_helper(board, word[1:], i, j-1):
        #         res = True
        #     board[i][j] = tmp
        #     return res
        
        # for i in range(m):
        #     for j in range(n):
        #         if exist_helper(board, word, i, j):
        #             return True
        # return False

        # m = len(board)
        # if m <= 0:
        #     return False
        # n = len(board[0])
        # if n <= 0:
        #     return False
        
        # def exist_helper(board, word, i, j):
        #     if len(word) <= 0:
        #         return True
        #     if i< 0 or i> m-1 or j < 0 or j > n-1:
        #         return False
        #     if board[i][j] != word[0]:
        #         return False
            

        #     tmp = board[i][j]
        #     board[i][j] = -1
        #     res = exist_helper(board, word[1:], i-1, j) or exist_helper(board, word[1:], i+1, j) or \
        #         exist_helper(board, word[1:], i, j-1) or exist_helper(board, word[1:], i, j+1)
        #     board[i][j] = tmp
            
        #     return res
        
        # for l in range(m):
        #     for o in range(n):
        #         if exist_helper(board, word, l, o):
        #             return True
                
        # return False
        

        # DO NOT UNPACK UNLESS NEEDED
        # m = len(board)
        # if m <= 0:
        #     return False
        # n = len(board[0])
        # if n <= 0:
        #     return False
        
        # def exist_helper(board, word, cur_pos):
        #     if len(word) <= 0:
        #         return True
        #     if i< 0 or i> m-1 or j < 0 or j > n-1:
        #         return False
        #     if board[i][j] != word[0]:
        #         return False
            

        #     tmp = board[i][j]
        #     board[i][j] = -1
        #     res = exist_helper(board, word[1:], (i-1, j)) or exist_helper(board, word[1:], (i+1, j)) or \
        #         exist_helper(board, word[1:], (i, j-1)) or exist_helper(board, word[1:], (i, j+1))
        #     board[i][j] = tmp
            
        #     return res
        
        # for l in range(m):
        #     for o in range(n):
        #         if exist_helper(board, word, (l, o)):
        #             return True
                
        # return False

                
            
        

                

        
        
# @lc code=end

