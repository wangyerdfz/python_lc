#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        if n == 0:
            return True
        result_list = [False] * n
        for i in reversed(range(n - 1)):
            result = False
            for word in wordDict:
                if s[]
        
# @lc code=end

