#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if len(s) == "0":
            return 0
        if len(s) == 1:
            if s == "0":
                return 0
            else:
                return 1


        res_len = [0] * n
        res_len[n-1] = self.numDecodings(s[-1])
        res_len[n-2] += self.numDecodings(s[n-1]) * self.numDecodings(s[n-2])
        if s[-2:] <= "26" and s[-2:] >= "10":
            res_len[n-2]+=1

        for i in range(n-3,-1,-1):
            if s[i] != "0":
                res_len[i]+= res_len[i+1]
            if s[i:i+2] <= "26" and s[i:i+2] >= "10":
                res_len[i] += res_len[i+2]

        return res_len[0]

# @lc code=end

