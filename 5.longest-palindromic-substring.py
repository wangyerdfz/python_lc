#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        max_len = 1
        max_start = 0
        max_end = 1
        for i in range(n):
            # check odd
            j = 1
            while (i - j >=0) and (i + j < n):
                if s[i - j] == s[i + j]:
                    if 2 * j + 1 > max_len:
                        max_len = 2 * j + 1
                        max_start = i - j
                        max_end = i + j + 1
                    j += 1
                else:
                    break

            # check even:
            j = 0
            while(i - j >= 0) and (i + j + 1 < n ):
                if s[i - j] == s[i + j + 1]:
                    if 2 * j + 2  > max_len:
                        max_len = 2 * j + 2
                        max_start = i - j
                        max_end = i + j + 2
                    j += 1
                else:
                        break

        return s[max_start:max_end]


        # n = len(s)
        # max_len = 0
        # max_str = ""
        # for i in range(n):
        #     # check odd
        #     j = 1
        #     while True:
        #         if ((i - j) < 0) or ((i + j) >= n) or s[i + j] != s[i - j] :
        #             break
        #         j+=1

        #     if 2 * (j - 1) + 1 > max_len:
        #         max_len = 2 * (j - 1) + 1
        #         max_str = s[i - j + 1: i + j ]

        # for i in range(n):
        #     # check even
        #     j = 1
        #     while True:
        #         if ((i - j + 1) < 0) or ((i + j) >= n) or s[i + j] != s[i - j + 1] :
        #             break
        #         j+=1

        #     if 2 * j - 2 > max_len:
        #         max_len = (2 * j - 2)
        #         max_str = s[i - j + 2: i + j]

        # return max_str


        
# @lc code=end

