#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        max_len = 0
        pos_map = {}
        prev_good = -1
        for i, char in enumerate(s):
            if char not in pos_map:
                pos_map[char] = i
                max_len = max(max_len, i - prev_good)
            else:
                prev_good = max(pos_map[char], prev_good) ## this max is so important!!!
                pos_map[char] = i
                max_len = max(max_len, i - prev_good)
        return max_len






# def lengthOfLongestSubstring(s: str) -> int:
#     n = len(s)
#     if n <= 1:
#         return n
#     max_len = 0
#     pos_map = {}
#     prev_good = -1
#     for i, char in enumerate(s):
#         print(f'i : {i}')
#         print(f'char : {char}')
#         print(f'map : {pos_map}')
#         print(f'max_len : {max_len}')
#         if char not in pos_map:
#             pos_map[char] = i
#             max_len = max(max_len, i - prev_good)
#         else:
#             prev_good = max(pos_map[char], prev_good)
#             pos_map[char] = i
#             max_len = max(max_len, i - prev_good)
#     return max_len


# if __name__ == '__main__':
#     test_str = "abba"
#     print(lengthOfLongestSubstring(test_str))




        # n = len(s)
        # if n <= 0:
        #     return 0
        # max_len = 0
        # for i in range(n):
        #     pos_map = {}
        #     for j in range(i, n):
        #         if s[j] not in pos_map:
        #             pos_map[s[j]] = True
        #             max_len = max(max_len, j - i + 1)
        #         else:
        #             break
        # return max_len






        # n = len(s)
        # max_len = 0
        # for i in range(n):
        #     reg = [0] * 128
        #     for j in range(i, n):
        #         if reg[ord(s[j])] >= 1:
        #             break
        #         max_len = max(max_len, j - i + 1)
        #         reg[ord(s[j])]+=1

        # return max_len
        
# @lc code=end

