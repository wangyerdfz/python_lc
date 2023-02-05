#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if n == 0:
            return True
        result_list = [False] * n
        for i in reversed(range(n )):
            result = False
            for word in wordDict:
                if s[i:].startswith(word):
                    if i + len(word) == n:
                        result = True
                    elif result_list[i + len(word)]:
                        result = True
                result_list[i] = result
        return result_list[0]
        

# @lc code=end

