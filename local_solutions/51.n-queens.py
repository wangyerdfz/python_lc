def solveNQueens(n: int) ->list:
    res = []

    def correct(queens:list, n_element):
        for i in range(n_element-1):
            if (abs(queens[i] - queens[n_element-1]) == n_element-1-i) or (queens[i] == queens[n_element-1]):
                return False
        return True

        
    def dfs(queens:list, n_element):
        if n_element == n:
            if correct(queens, n_element):
                res.append(queens.copy())
            return 

        for i in range(n):
            queens[n_element] = i
            if correct(queens, n_element+1):
                dfs(queens.copy(), n_element+1)

        return

    def convert_to_board(queens:list):
        board = [['.'] * n  for _ in range(n)]
        for row, col in enumerate(queens):
            board[row][col] = 'Q'
        
        board = [''.join(x) for x in board]
        return board

    queens_ = [-1]*n
    dfs(queens_, 0)

    print(res)
    return [convert_to_board(x) for x in res]



if __name__ == '__main__':
    print(solveNQueens(4))