#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ret_list = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            temp_list = [1]
            for j in range(1, i - 1):
                temp_list.append(ret_list[i - 2][j -1 ] + ret_list[i - 2][j ])
            temp_list.append(1)
            ret_list.append(temp_list)
        return ret_list


# def generate(numRows):
#     if numRows == 1:
#         return [[1]]
#     if numRows == 2:
#         return [1, 1]
#     ret_list = [[1], [1, 1]]
#     for i in range(3, numRows + 1):
#         temp_list = [1]
#         for j in range(1, i - 1):
#             print(ret_list)
#             temp_list.append(ret_list[i - 2][j -1 ] + ret_list[i - 2][j ])
#         temp_list.append(1)
#         ret_list.append(temp_list)
#     return ret_list

# if __name__ == '__main__':
#     print(generate(5))

# @lc code=end

