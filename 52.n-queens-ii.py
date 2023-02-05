#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        queens = [-1] * n

        def dfs(index):
            if index == len(queens):
                res.append(queens.copy())
                return
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):
                    dfs(index + 1)

        def valid(n):
            for i in range(n):
                if (abs(queens[i] - queens[n]) == n - i) or (queens[i] == queens[n]):
                    return False
            return True 

        def make_board(queens):
            n = len(queens)
            board = []
            board_tmp = [['.']* n for _ in range(n)]
            for row, col in enumerate(queens):
                board_tmp[row][col] = 'Q'
            for row in board_tmp:
                board.append("".join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards


        dfs(0)
        return len(make_all_boards(res))
# @lc code=end

