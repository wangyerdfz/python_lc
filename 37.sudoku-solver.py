#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        """
        Do not return anything, modify board in-place instead.
        """
        def check(board, i, j, val):
            row = i - i%3
            column = j - j%3
            for x in range(9):
                if board[i] [x] == val:
                    return False
            for y in range(9):
                if board[y][j] == val:
                    return False

            for x in range(3):
                for y in range(3):
                    if board[row + x][column + y] == val:
                        return False


            return True


        def solve_soduku_helper(board, i, j):
            if i >= 9:
                return True
            if j >= 9:
                return solve_soduku_helper(board, i+1, j%9)
            
            if board[i][j] != '.':
                return solve_soduku_helper(board, i, j+1)

            for c in [str(x) for x in range(1, 10)]:
                if check(board = board, i = i, j = j, val = c):
                    board[i][j] = c
                    if solve_soduku_helper(board, i, j+1):
                        return True
                    board[i][j] = '.'


            return False

        return solve_soduku_helper(board, 0, 0)




# @lc code=end

