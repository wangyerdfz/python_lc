#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_valid_block(block : list) -> bool:
            for i in range(1, 10):
                if block.count(str(i)) > 1:
                    return False
            return True
        check_list = []
        for i in range(9):
            check_list.append( [board[i][j] for j in range(9)])
        for i in range(9):
            check_list.append( [board[j][i] for j in range(9)])
        for i in range(3):
            for j in range(3):
                tmp_list = []
                tmp_list += [board[i * 3][j * 3 + k] for k in range(3)]
                tmp_list += [board[i * 3 + 1][j * 3 + k] for k in range(3)]
                tmp_list += [board[i * 3 + 2][j * 3 + k] for k in range(3)]
                check_list.append( tmp_list)
        for tmp_list in check_list:
            if not check_valid_block(tmp_list):
                return False

        return True
        
        
# @lc code=end

