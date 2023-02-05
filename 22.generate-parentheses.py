#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen_par_helper(left : int, right: int) -> list:
            if left < 0 or right < 0:
                return []
            if left == 0 and right == 1:
                return [")"]
            if left == 0 and right == 0:
                return []
            if left > right :
                return []
            if left == right:
                return ["(" + x for x in gen_par_helper(left - 1, right)]
            return [")" + x for x in gen_par_helper(left, right - 1)] + \
                ["(" + x for x in gen_par_helper(left - 1, right)]
        
        if n <= 0:
            return []
        return gen_par_helper(n, n)













#         def gen_parenthesis_helper(left_num : int, right_num : int) -> List[str]:
#             if left_num == 0:
#                 if right_num == 0:
#                     return [""]
#                 return [")" + x for x in gen_parenthesis_helper(0, right_num - 1)]
#             if left_num == right_num:
#                 return ["(" + x for x in gen_parenthesis_helper(left_num - 1, right_num )]
#             else:
#                 return [")" + x for x in gen_parenthesis_helper(left_num, right_num - 1)] + \
#                     ["(" + x for x in gen_parenthesis_helper(left_num - 1, right_num )]
#         if n <= 0:
#             return []
#         return gen_parenthesis_helper(n, n)




# def generateParenthesis(n: int) -> list:
#     def gen_parenthesis_helper(left_num : int, right_num : int) -> list:
#         if left_num == 0:
#             if right_num == 0:
#                 return [""]
#             return [")" + x for x in gen_parenthesis_helper(0, right_num - 1)]

#         if left_num == right_num:
#             return ["(" + x for x in gen_parenthesis_helper(left_num - 1, right_num )]
#         else:
#             return [")" + x for x in gen_parenthesis_helper(left_num, right_num - 1)] + \
#                 ["(" + x for x in gen_parenthesis_helper(left_num - 1, right_num )]


#     if n <= 0:
#         return []
#     return gen_parenthesis_helper(n, n)


# if __name__ == '__main__':
#     n = 10
#     res = generateParenthesis(n)
#     print(res)
#     print(len(res))

# @lc code=end

