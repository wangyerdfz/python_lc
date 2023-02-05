#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        if m <= 0 or n <= 0:
            return res
        cur_x, cur_y = 0, 0
        cur_dir = "right"
        turn_count = 0


        def move(x, y, dir):
            if dir == "right":
                return x, y + 1
            if dir == "down":
                return x+1, y
            if dir == "left":
                return x, y-1
            else:
                return x-1, y

        def out_of_bound(x, y, m, n):
            if x < 0 or x >= m:
                return True
            if y < 0 or y >= n:
                return True
            return False

        def turn_right(dir):
            if dir == "right":
                return "down"
            if dir == "down":
                return "left"
            if dir == "left":
                return "up"
            return "right"

        while True:
            if turn_count == 0:
                res.append(matrix[cur_x][cur_y])
                matrix[cur_x][cur_y] = -20000
            next_x, next_y = move(cur_x, cur_y, cur_dir)
            if (not out_of_bound(next_x, next_y, m, n)) and matrix[next_x][next_y] > - 2000:
                cur_x, cur_y = next_x, next_y
                turn_count = 0
            else:
                cur_dir = turn_right(cur_dir)
                turn_count += 1
            if turn_count > 3:
                break
        
        return res

                    
# @lc code=en

