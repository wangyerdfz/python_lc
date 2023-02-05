#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        
        def turn_right(dir_):
            if dir_ == 'right':
                return 'down'
            if dir_ == 'down':
                return 'left'
            if dir_ == 'left':
                return 'up'
            else:
                return 'right'
            
        def move(cor_, dir_):
            if dir_ == 'right':
                return (cor_[0], cor_[1]+1)
            if dir_ == 'down':
                return (cor_[0]+1, cor_[1])
            if dir_ == 'left':
                return (cor_[0], cor_[1]-1)
            else:
                return (cor_[0]-1, cor_[1])
            
        def if_out_of_bound_or_filled(cor_, board):
            if (cor_[0] < 0) or (cor_[0] >= n) or (cor_[1] < 0) or (cor_[1] >= n) or (board[cor_[0]][cor_[1]] != -1):
                return True
            return False
        

        board = [[-1]* n for _ in range(n)]
        cor_ = (0, 0)
        dir_ = 'right'
        for num_ in range(n * n):
            board[cor_[0]][cor_[1]] = num_+1
            next_cor_ = move(cor_, dir_)
            if if_out_of_bound_or_filled(next_cor_, board):
                dir_ = turn_right(dir_)
                next_cor_ = move(cor_, dir_)
            cor_ = next_cor_

        return board
# @lc code=end

