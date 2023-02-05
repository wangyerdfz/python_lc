#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def correct(queens:list, n_element):
            for i in range(n_element-1):
                if (queens[i] - queens[n-1] == abs(n-1-i)) or (queens[i] == queens[n-1]):
                    return False
                return True

            
        def dfs(queens:list, n_element):
            if n_element == n:
                if correct(queens.copy(), n_element):
                    res.append(queens)
                return 

            for i in range(n):
                queens[n_element] = i
                dfs(queens.copy(), n_element+1)

        def convert_to_board(queens:list):
            board = [['.'] * n ]*n
            for row, col in enumerate(queens):
                board[row][col] = 'Q'
            
            board = [''.join(x) for x in board]
            return board

        queens_ = [-1]*n
        dfs(queens_, 0)
        return [convert_to_board(x) for x in res]
        # res = []
        # queens = [-1] * n

        # def dfs(index):
        #     if index == len(queens):
        #         res.append(queens.copy())
        #         return
        #     for i in range(len(queens)):
        #         queens[index] = i
        #         if valid(index):
        #             dfs(index + 1)

        # def valid(n):
        #     for i in range(n):
        #         if (abs(queens[i] - queens[n]) == n - i) or (queens[i] == queens[n]):
        #             return False
        #     return True 

        # def make_board(queens):
        #     n = len(queens)
        #     board = []
        #     board_tmp = [['.']* n for _ in range(n)]
        #     for row, col in enumerate(queens):
        #         board_tmp[row][col] = 'Q'
        #     for row in board_tmp:
        #         board.append("".join(row))
        #     return board

        # def make_all_boards(res):
        #     actual_boards = []
        #     for queens in res:
        #         actual_boards.append(make_board(queens))
        #     return actual_boards


        # dfs(0)
        # return make_all_boards(res)
        
# @lc code=end

