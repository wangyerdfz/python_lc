#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        n = len(s)
        str_list = []
        i = 0
        while i < n: # first row
            str_list.append(s[i])
            i += 2 * (numRows - 1)
        
        for row_num in range(1, numRows -1): # mid row
            stop_mark = False
            i = row_num
            j = 2 * numRows - 2 - row_num
            while not stop_mark:
                if i < n:
                    str_list.append(s[i])
                    i = i + 2 * (numRows - 1)
                else:
                    stop_mark = True
                if j < n:
                    str_list.append(s[j])
                    j = j + 2 * (numRows - 1)
                else:
                    stop_mark = True
        stop_mark = False
        i = numRows - 1
        while not stop_mark:
            if i < n:
                str_list.append(s[i])
                i = i + 2*(numRows - 1)
            else:
                stop_mark = True
        
        return "".join(str_list)

            
                

        
# @lc code=end

