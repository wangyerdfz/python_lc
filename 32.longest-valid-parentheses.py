#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        max_ = 0
        idx_stack = [-1]
        for i, cur_tok in enumerate(s):
            if cur_tok == "(":
                idx_stack.append(i)
            else:
                idx_stack.pop()
                if idx_stack:
                    max_ = max(i - idx_stack[-1], max_)
                else:
                    idx_stack.append(i)
        
        return max_
                    
        


# def longestValidParentheses(s: str) -> int:
#     n = len(s)
#     if n == 0:
#         return 0
#     max_ = 0
#     i = 0
#     while (i < n):
#         count = 0
#         if s[i] != "(":
#             i += 1
#             continue
#         count += 1
#         for j in range(i + 1, n):
#             if s[j] == "(":
#                 count += 1
#                 continue
#             count -= 1
#             if count < 0:
#                 i = j
#                 break
#             if count == 0:
#                 max_ = max(max_, j - i + 1)
#                 print(i, j)
#         i += 1
#     return max_

# if __name__ == '__main__':
#     target_str = "(())()(()(("
#     print(longestValidParentheses(target_str))
# @lc code=end

